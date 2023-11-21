import sqlite3
from datetime import datetime, timedelta

def hours_checker():

    conn = sqlite3.connect('MonthAttendance.db')
    cursor = conn.cursor()

    cursor.execute('''
         SELECT employee_id,
                employee_name,
                date, 
                arrival_time,
                leave_time
                FROM attendance   
            ''')
    
    workers_data = cursor.fetchall()
    overtime = {}

    for worker_data in workers_data:
        employee_id = str(worker_data[0])
        employee_name = worker_data[1]
        date = worker_data[2]
        arrival_time = datetime.strptime(worker_data[3], '%Y-%m-%d %H:%M')
        leave_time = datetime.strptime(worker_data[4], '%Y-%m-%d %H:%M')

        working_time = (leave_time - arrival_time).total_seconds() / 60
        difference_minutes = working_time - 480
        overtime[date] = max(0, difference_minutes)

        if difference_minutes < 0:
            print(f"Pre {date}: Chýbajú {abs(difference_minutes)} minúty.") 

    return overtime

hours_checker()

        




