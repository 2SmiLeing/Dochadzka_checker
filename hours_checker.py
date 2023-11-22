import sqlite3
from datetime import datetime, timedelta
from workersData import selected_year, selected_month

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
    #overtime = {}
    overtime_minutes = 0

    for worker_data in workers_data:
        employee_id = str(worker_data[0])
        employee_name = worker_data[1]
        date = worker_data[2]
        arrival_time_str = worker_data[3]
        leave_time_str = worker_data[4]

        print("-------------------------------------------")
        print(f"Processing data for {employee_name}, date: {date}, arrival: {arrival_time_str}, leave: {leave_time_str}")

        arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%d %H:%M')
        leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M')

        working_time = (leave_time - arrival_time).total_seconds() / 60
        difference_minutes = working_time - 480
        #overtime[date] = max(0, difference_minutes)

        if difference_minutes < 0:
            print(f"For {date}: Missing {abs(difference_minutes)} minutes.")
            print("-------------------------------------------")
            overtime_minutes -= difference_minutes            

        elif difference_minutes >= 0:
            print(f"For {date}: Overtime {abs(difference_minutes)} minutes.")
            print("-------------------------------------------")
            overtime_minutes += difference_minutes

        
        
    print(f"For {selected_year} year and {selected_month} month: Worker {employee_name} whit ID {employee_id} have {overtime_minutes} minutes overtime/missing. ")

hours_checker()

        




