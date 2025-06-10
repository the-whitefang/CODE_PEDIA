# ********** Testing the Email-Shooting upon getting any Gap time. ********** #

import mysql.connector
import pandas as pd 
from datetime import timedelta, datetime
import yagmail

# ----- Configuration ----- #
db = {
    'host':"192.167.150.27",
    'user':"****r",
    'password':"Cdhfshssn",
    'database':"database",
    'port':'3246'
}

Tb_name= 'checklist_data'
Created_Column = 'created_at'

Email_user = 'sample@gmail.com'
Email_pass = 'jndcbwc'
Email_to = 'sample@gmail.com'

# ----- Fetching Data from the DB ----- #
def get_data():
    conn = mysql.connector.connect(**db)
    sql_script = f"SELECT {Created_Column} FROM {Tb_name} ORDER BY {Created_Column}"
    data = pd.read_sql(sql_script, conn)
    conn.close()
    return data

# ----- function to check for the missing data in 15 mins interval ----- #
def missing_data_verification(data):
    data[Created_Column] = pd.to_datetime(data[Created_Column])
    data.set_index(Created_Column, inplace= True)
    
    full_range = pd.date_range(start=data.index.min(), end= data.index.max(), freq= '15T')
    gap_time = full_range.difference(data.index)
    
    if gap_time.empty:
        return []
    
    gap_periods = []
    gap_start = gap_time[0]
    
    for i in range(1, len(gap_time)):
        if (gap_time[i] - gap_time[i-1]) != timedelta(minutes=15):
            gap_end = gap_time[i-1]
            duration = (gap_end - gap_start).total_seconds() / 60
            if duration >= 30:
                gap_periods.append((gap_start, gap_end + timedelta(minutes=15)))
            gap_start = gap_time[i]
    
    if (gap_time[-1] - gap_start).total_seconds() / 60 >= 30:
        gap_periods.append((gap_start, gap_time[-1] + timedelta(minutes=15)))
    
    return gap_periods

# ----- function to shoot email upon checking if the data is missing for more than 30 minutes -----#
def email_shooting(gaps):
    if not gaps:
        print("No gaps present.")
        return
    
    yag = yagmail.SMTP(Email_user, Email_pass)

    body = "There is some problem with data parsing between the following times:\n\n"
    for start, end in gaps:
        body += f"From {start} to {end}\n"

    body += "\nPlease immediately look into this matter urgently! and the continue parsing the data as soon as possible."

    yag.send(
        to=Email_to,
        subject="Alert: Data Entry Missing",
        contents=body
    )
    print("Alert! email sent!")

if __name__ == "__main__":
    data = get_data()
    gaps = missing_data_verification(data)
    email_shooting(gaps)