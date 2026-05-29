import sys
import io
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.environ["GOOGLE_API_KEY"] = "AIzaSyAcQbq_kBvbB3UV_1K6Stx-qbE-yihc0Bs" 

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
db = SQLDatabase.from_uri("sqlite:///my_database.db")

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

print("--- HỆ THỐNG TRUY VẤN DỮ LIỆU BẰNG TIẾNG VIỆT ---")
while True:
    user_query = input("\nBạn muốn hỏi gì về dữ liệu? (hoặc gõ 'thoát'): ")
    if user_query.lower() == 'thoát':
        break
    
    try:
        result = db_chain.invoke(user_query)
        
        print(f"\n[AI Trả Lời]: {result['result']}")
        
    except Exception as e:
        print(f"\n[Lỗi]: AI không hiểu hoặc câu lệnh SQL sai. Chi tiết: {e}")
