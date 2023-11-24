import sqlite3
from datetime import datetime, timedelta
import calendar
import time

width = 140

def print_with_delay(text, delay=0.02):
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)

def input_year_month():
    text = ("*" * 25 + "  Zadajte rok a mesiac, pre ktory chcete zistit dochadzku  " + "*" * 25)
    centered_text = text.center(width)
    print_with_delay(centered_text)
    print("\n")
    
    while True:
        year_input = input("Zadajte rok: ")
        month_input = input("Zadajte mesiac: ")
        print_with_delay("\n-------------------------------------------\n", 0.01)        

        if len(year_input) != 4 or not year_input.isdigit() or not month_input.isdigit() or not 1 <= int(month_input) <= 12:
            print("Neplatný vstup. Rok musí byť štvorciferné celé číslo a mesiac musí byť dvojciferné celé číslo medzi 1 a 12.")
        else:
            return int(year_input), int(month_input)

selected_year, selected_month = input_year_month()

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
    print("\n")
    name_or_id = input("Zadajte meno alebo ID zamestnanca: ").title()

    filtered_data = []

    for worker_data in workers_data:
        employee_id = str(worker_data[0])
        employee_name = worker_data[1]
        
        if str(worker_data[0]) == name_or_id or worker_data[1] == name_or_id:
            date_parts = worker_data[2].split("-")
            data_year, data_month = int(date_parts[0]), int(date_parts[1])
            
            if data_year == selected_year and data_month == selected_month:
                filtered_data.append(worker_data)

    overtime_minutes = 0

    for worker_data in filtered_data:
        employee_id, employee_name = str(worker_data[0]), worker_data[1]
        date = worker_data[2]
        arrival_time_str = worker_data[3]
        leave_time_str = worker_data[4]

        print_with_delay("\n-------------------------------------------\n", 0.01)
        print_with_delay(f"ID: {employee_id}, Meno: {employee_name}, Dátum: {date}, Príchod: {arrival_time_str}, Odchod: {leave_time_str}")
        time.sleep(0.01)  
        
        arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%d %H:%M')
        leave_time = datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M') or datetime.strptime(leave_time_str, '%Y-%m-%d %H:%M') + timedelta(days=1)

        working_time = (leave_time - arrival_time).total_seconds() / 60
        difference_minutes = working_time - 480

        if difference_minutes < 0:
            print_with_delay(f"\n {date}: Missing {abs(difference_minutes)} minutes.")
            print_with_delay("\n-------------------------------------------\n", 0.01)
            overtime_minutes += difference_minutes
            print_with_delay(f"Overtime: {overtime_minutes}")
            

        elif difference_minutes >= 0:
            print_with_delay(f"\n {date}: Overtime {abs(difference_minutes)} minutes.")
            print_with_delay("\n-------------------------------------------\n", 0.01)
            overtime_minutes += difference_minutes
            print_with_delay(f"Overtime: {overtime_minutes}")

    print("\n\n")
    print_with_delay(f"For year {selected_year} and month {selected_month}: Worker {employee_name} with ID {employee_id} have {overtime_minutes} minutes overtime/missing. ")
    print("\n\n")

hours_checker()


        






        




