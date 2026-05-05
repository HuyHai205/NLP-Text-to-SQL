import pandas as pd
import sqlite3

df = pd.read_csv('employee_records.csv') 

# Bạn có thể in thử 5 dòng đầu tiên để xem data đã load thành công chưa
print("Dữ liệu gốc:")
print(df.head())

# 2. Tạo kết nối đến file Database SQLite 
# Nếu file 'my_database.db' chưa có, Python sẽ tự động tạo file mới
conn = sqlite3.connect('my_database.db')

# 3. Đổ toàn bộ dữ liệu từ DataFrame vào bảng SQL
# 'students_table' là tên bảng sẽ được tạo trong Database
df.to_sql('students_table', conn, if_exists='replace', index=False)

# 4. Đóng kết nối
conn.close()

print("\nĐã chuyển đổi thành công từ CSV sang SQLite database!")