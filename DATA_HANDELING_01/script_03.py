''' ********** Now as per the requirement this script will check for the missing data entry time gaps
         and if found any will shoot mail alerting to look into the matter asap. The checking will happen for 
         every 30 mins and the max threshold will be 2 hours after which an alert mail will be sent, and continuing
         that another 30 mins follow-up window will be set and if the data is missing for that window also then 
         one more alert mail will be sent.
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import mysql.connector
import pandas as pd 
from datetime import datetime, timedelta
import yagmail

sender_email_user = "sample@gmail.com"
sender_email_password = "jndcbwc"
receiver_email = "sample@gmail.com"

database_configuration = {
    'host': '192.167.150.27',
    'user': '****r',
    'password': 'Cdhfshssn',
    'database': 'database',
    'port': '3246'
}

last_alert_endTime = None

def missing_data_verification():
    global last_alert_endTime
    print(f"Running check at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        conn = mysql.connector.connect(**database_configuration)
        cursor = conn.cursor()
        
        query = "SELECT created_at FROM checklist_data ORDER BY created_at"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        data = pd.DataFrame(rows, columns=['created_at'])
        data['created_at'] = pd.to_datetime(data['created_at'])
        data.sort_values(by='created_at', inplace=True)
        gap_time = data['created_at'].tolist()
        
        gap_max_limit = timedelta(hours=2)
        followup_gap_check = timedelta(minutes= 30)
        gaps = []
        
        for i in range(len(gap_time) - 1):
            diff = gap_time[i + 1] - gap_time[i]
            if diff >= gap_max_limit:
                gap_start = gap_time[i]
                gap_end = gap_time[i + 1]
                gaps.append((gap_start, gap_end))
                
                if last_alert_endTime is None or gap_end > last_alert_endTime:
                    mail_shoot(f"Data Missing from {gap_start} to {gap_end} (2+ hours gap)")
                    last_alert_endTime = gap_end
                    
                    followup_Data_Verification(gap_end, gap_end + followup_gap_check)
        
        if not gaps:
            print("No 2 hours Data gaps were detected. ")
        
        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"Error Occurred: {e}")

def followup_Data_Verification(start_time, end_time):
    try: 
        conn = mysql.connector.connect(**database_configuration)
        cursor = conn.cursor()
        
        
        sql_script = f""" 
            SELECT COUNT(*) FROM checklist_data
            WHERE created_at > '{start_time.strftime('%Y-%m-%d %H:%M:%S')}'
            AND created_at <= '{end_time.strftime('%Y-%m-%d %H:%M:%S')}'
        """
        
        cursor.execute(sql_script)
        count = cursor.fetchone()[0]
        
        if count == 0:
            mail_shoot(f"No data found for 30 minutes after the previous 2 hour Gap time ({start_time} to {end_time})")
        
        cursor.close()
        conn.close()
    
    except Exception as e:
        print(f"Error in follow-up verification: {e}")


def mail_shoot(body_text_part):
    try:
        subject = "Data Entry Missing Alert! "
        yag = yagmail.SMTP(sender_email_user, sender_email_password)
        yag.send(receiver_email, subject, body_text_part)
        print(f"The E-mail has been sent: {subject}")
    
    except Exception as e:
        print(f" Failed to send the mail: {e}")


scheduler = BlockingScheduler()
trigger = CronTrigger(minute='0, 30', hour='9-21')

scheduler.add_job(missing_data_verification, trigger)

try:
    print("Scheduler started: Runs every 30 mins from 9 AM to 10 PM")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Scheduler Stopped.")