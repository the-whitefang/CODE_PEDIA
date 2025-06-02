import sqlite3

conn = sqlite3.connect("employee_records.db")
cursor = conn.cursor()

# Count total records
cursor.execute("SELECT COUNT(*) FROM employees")
print("Total records:", cursor.fetchone()[0])

# Count per date
cursor.execute("SELECT created_at, COUNT(*) FROM employees GROUP BY created_at")
for row in cursor.fetchall():
    print(row)

conn.close()
