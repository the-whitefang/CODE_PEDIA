import sqlite3
import random
from datetime import date, timedelta


first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivan", "Judy"]
last_names = ["Smith", "Johnson", "Lee", "Brown", "Wilson", "Moore"]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]


conn = sqlite3.connect('employee_records.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER,
        emp_name TEXT NOT NULL,
        emp_city TEXT NOT NULL,
        emp_tenure INTEGER NOT NULL,
        emp_salary INTEGER NOT NULL,
        created_at DATE NOT NULL
    )
    """
)

start_date = date(2025, 5, 1)

for day_offset in range(30):  # For 30 days
    current_date = start_date + timedelta(days=day_offset)
    for emp_id in range(1, 101):  # 100 records per day
        emp_name = random.choice(first_names) + " " + random.choice(last_names)
        emp_city = random.choice(cities)
        emp_tenure = random.randint(0, 30)
        emp_salary = random.randint(30000, 150000)
        
        cursor.execute("""
            INSERT INTO employees (emp_id, emp_name, emp_city, emp_tenure, emp_salary, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (emp_id, emp_name, emp_city, emp_tenure, emp_salary, current_date))




conn.commit()
conn.close()