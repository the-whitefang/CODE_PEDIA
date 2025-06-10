# ********** Using the Scheduler Library the Script has be bound for every day 9 AM to 10 AM. ********** #
# ***** The Missing data check for every 15 mins, and the max missing data threshold is set for 30 mins. ***** #

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import mysql.connector
import pandas as pd 
from datetime import datetime, timedelta
import yagmail

Sender_User_mail = "sample@gmail.com"
User_mail_app_password = "jndcbwc"
Receiver_User_mail = "sample@gmail.com"


Database_Config = {
    'host': '192.167.150.27',
    'user': '****r',
    'password': "Cdhfshssn",
    'database': 'database',
    'port': '3246'
}

def missing_data_verification():
    try:
        print(f"Checking at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        conn = mysql.connector.connect(**Database_Config)
        cursor = conn.cursor()
        
        query = "SELECT created_at FROM checklist_data ORDER BY created_at"
        cursor.execute(query)
        rows = cursor.fetchall()
        data = pd.DataFrame(rows, columns=['created_at'])
        data['created_at'] = pd.to_datetime(data['created_at'])
        
        data.sort_values(by='created_at', inplace=True)
        gap_time = data['created_at'].to_list()
        
        gap_threshold = timedelta(minutes=30)
        gaps = []
        
        for i in range(len(gap_time) - 1):
            diff = gap_time[i + 1] - gap_time[i]
            if diff >= gap_threshold:
                gaps.append((gap_time[i], gap_time[i + 1]))
        
        if gaps:
            message = "There is some problem with data parsing between the following times:\n\n"
            for start, end in gaps:
                message += f" -> Gap from {start} to {end}, -> (Duration: {end - start})\n"
            
            message += "\nPlease immediately look into this matter urgently! and the continue parsing the data as soon as possible."
            
            mail_shoot = yagmail.SMTP(Sender_User_mail, User_mail_app_password)
            mail_shoot.send(Receiver_User_mail, "Data Missing Alert! ", message)
            print("Alert mail sent. ")
        else:
            print("No Data Gaps found.")
        
        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"Error occurred: {e}")

scheduler = BlockingScheduler()
trigger = CronTrigger(minute='0,15,30,45', hour='9-21')

scheduler.add_job(missing_data_verification, trigger)

try:
    print("Scheduler started: Runs every 15 mins between 3pm and 4pm")
    scheduler.start()

except (KeyboardInterrupt, SystemExit):
    print("Scheduler stopped")