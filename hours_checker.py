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

    for worker_data in workers_data:
        employee_id = str(worker_data[0])
        employee_name = worker_data[1]
        date = worker_data[2]
        arrival_time = worker_data[3]
        leave_time = worker_data[4]

        print(date)
        print(arrival_time)
        print(leave_time)


        #print(employee_id)
        #print(employee_name)




hours_checker()

        




