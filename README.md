# 🤖 Trợ lý Phân tích Dữ liệu AI (Text-to-SQL)

Dự án này là một hệ thống **Hỏi đáp Dữ liệu tự động (Text-to-SQL)**, cho phép người dùng truy vấn cơ sở dữ liệu (Database) bằng ngôn ngữ tự nhiên (tiếng Việt) mà không cần biết viết mã SQL. 

Thay vì phải gõ các câu lệnh `SELECT`, `JOIN` phức tạp, người dùng chỉ cần hỏi: *"Tìm 5 nhân viên có mức lương cao nhất"*, AI sẽ tự động dịch câu hỏi, truy xuất dữ liệu và trả lời bằng tiếng Việt.

## 🚀 Tính năng nổi bật
* **Hiểu ngôn ngữ tự nhiên (NLP):** Nhận diện chính xác ý định của người dùng bằng tiếng Việt.
* **Tự động tạo SQL (Text-to-SQL):** Chuyển đổi ngôn ngữ tự nhiên thành câu lệnh SQL chuẩn xác.
* **Tự động thực thi:** Chạy trực tiếp câu lệnh SQL trên Database cục bộ (SQLite) để lấy dữ liệu thực tế.
* **Giao diện thân thiện:** Tương tác mượt mà qua giao diện Web được xây dựng bằng Streamlit.

## 🛠 Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.10+
* **LLM (Large Language Model):** Google Gemini 2.5 Flash
* **AI Framework:** LangChain (LangChain Experimental SQL)
* **Cơ sở dữ liệu:** SQLite (Tích hợp sẵn)
* **Giao diện Web:** Streamlit

## ⚙️ Kiến trúc Hệ thống (Workflow)
Hệ thống hoạt động theo đường ống (Pipeline) 4 bước:
1. **Input:** Người dùng nhập câu hỏi bằng tiếng Việt qua giao diện Web.
2. **Translation:** LangChain gửi câu hỏi và cấu trúc Database (Schema) cho mô hình Gemini. Gemini sẽ suy luận và viết ra câu lệnh SQL tương ứng.
3. **Execution:** LangChain nhận câu lệnh SQL, chọc vào file `my_database.db` để lấy dữ liệu thô.
4. **Output:** Kết quả dữ liệu thô được AI tổng hợp lại thành câu trả lời tiếng Việt tự nhiên và hiển thị lên màn hình.

## 💻 Hướng dẫn Cài đặt & Chạy trên máy cá nhân

**Bước 1: Clone dự án về máy**
> git clone https://github.com/HuyHai205/NLP-Text-to-SQL.git
> cd NLP-Text-to-SQL

**Bước 2: Tạo môi trường ảo và cài thư viện**
> python3 -m venv .venv
> source .venv/bin/activate
> pip install langchain-google-genai langchain-community langchain-experimental streamlit sqlalchemy pandas

**Bước 3: Cấu hình API Key**
* Mở file `app_web.py`.
* Tìm dòng `os.environ["GOOGLE_API_KEY"] = "..."` và dán API Key Gemini của bạn vào. *(Lưu ý: Không chia sẻ Key này công khai).*

**Bước 4: Chạy giao diện Web**
> python -m streamlit run app_web.py

Hệ thống sẽ tự động mở trang web trên trình duyệt tại địa chỉ: `http://localhost:8501`

---
*Dự án được phát triển bởi Nguyễn Huy Hải.*
