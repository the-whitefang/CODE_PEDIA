import sqlite3
from datetime import date, timedelta


conn = sqlite3.connect("employee_records.db")
cursor = conn.cursor()


cutoff_date = date.today() - timedelta(days=30)
cutoff_date_str = cutoff_date.isoformat() 


cursor.execute("DELETE FROM employee WHERE created_at <= ?", (cutoff_date_str,))


conn.commit()
conn.close()
