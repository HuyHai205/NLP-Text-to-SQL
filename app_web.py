import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

st.set_page_config(page_title="AI SQL Assistant")
st.title(" Trợ lý Phân tích Dữ liệu (Text-to-SQL)")
st.markdown("Nhập câu hỏi bằng tiếng Việt, AI sẽ tự động truy vấn Database và trả kết quả cho bạn!")

os.environ["GOOGLE_API_KEY"] = "" 

# Khởi tạo model (Dùng bản 2.5 Flash của Google)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

db = SQLDatabase.from_uri("sqlite:///my_database.db")

db_chain = SQLDatabaseChain.from_llm(
    llm, 
    db, 
    verbose=True, 
    return_intermediate_steps=True
)

user_query = st.text_input("Nhập câu hỏi của bạn (vd: Hiển thị top 5 người có mức lương cao nhất):")

if st.button("Truy vấn Data"):
    if user_query:
        with st.spinner("AI đang phân tích và chạy lệnh SQL..."):
            try:
                strict_query = user_query + "\nHãy trả lời bằng một câu tiếng Việt tự nhiên dựa trên dữ liệu. TUYỆT ĐỐI KHÔNG in lại code SQL hay chữ 'SQLQuery' vào câu trả lời."
                
                response = db_chain.invoke(strict_query)
                st.success("Truy vấn thành công!")
                
                final_answer = response.get("result", "Không có câu trả lời.")
                
                sql_query = "Không tìm thấy code SQL."
                steps = response.get("intermediate_steps", [])
                
                for step in steps:
                    if isinstance(step, str) and step.strip().upper().startswith("SELECT"):
                        sql_query = step.strip()
                        break  
                    elif isinstance(step, dict) and "sql_cmd" in step:
                        sql_query = step["sql_cmd"]
                        break

                if "SQLQuery:" in final_answer:
                    final_answer = "Dạ, tôi đã tra cứu xong dữ liệu. (AI đang hơi lười tổng hợp, bạn xem tạm kết quả ở câu lệnh SQL bên trên nhé!)"
                else:
                    final_answer = final_answer.replace("Answer:", "").replace("Question:", "").strip()

                st.write("** Câu lệnh SQL được tạo ra:**")
                st.code(sql_query, language="sql") 
                
                st.write("**Câu trả lời của AI:**")
                st.info(final_answer)
                
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {e}")
    else:
        st.warning("Vui lòng nhập câu hỏi trước khi bấm nút!")











    
