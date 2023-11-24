import sqlite3
from employees import *
from datetime import datetime, timedelta
import calendar
import random
import time

width = 140
def print_with_delay(text, delay=0.02):
        for char in text:
            time.sleep(delay)
            print(char, end='', flush=True)

def input_year_month():
    while True:
        text = ("*" * 25 + "  Zadajte rok a mesiac, pre ktory chcete vygenerovat dochadzku  " + "*" * 25)
        centered_text = text.center(width)
        print_with_delay(centered_text)
        print("\n")
        year_input = input("Zadajte rok: ")
        month_input = input("Zadajte mesiac: ")

        if len(year_input) != 4 or not year_input.isdigit() or not month_input.isdigit() or not 1 <= int(month_input) <= 12:
            print("Neplatný vstup. Rok musí byť štvorciferné celé číslo a mesiac musí byť dvojciferné celé číslo medzi 1 a 12.")
        else:
            return int(year_input), int(month_input)
        
selected_year, selected_month = input_year_month()


_, days_in_month = calendar.monthrange(selected_year, selected_month)
workdays_count = 0

for day in range(1, days_in_month + 1):
    weekday = calendar.weekday(selected_year, selected_month, day)
    if 0 <= weekday <= 4:
        workdays_count += 1

print("")
print(f"V mesiaci {selected_year}-{selected_month} je {workdays_count} pracovních dní.")
print("")

cal = calendar.month(selected_year, selected_month)

print("")
print(f"Kalendar pre {calendar.month_name[selected_month]} {selected_year}:\n{cal}")
print("")



def databaze():
    conn = sqlite3.connect('dochazka.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dochazka (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            date DATE,
            arrival_time TIME,
            leave_time TIME
        )
    ''')

    _, days_in_month = calendar.monthrange(selected_year, selected_month)
    workdays = [day for day in range(1, days_in_month + 1) if 0 <= calendar.weekday(selected_year, selected_month, day) <= 4]

    generated_hours = []
    
    for workday in range(1, days_in_month + 1):
        # Kontrola, zda je den v pracovním týdnu (pondělí až pátek)
        current_date = datetime(selected_year, selected_month, workday)
        if current_date.weekday() < 5:
            generated_hours.append(current_date)

            for employee_id, employee_name in employees.items():
                date = f"{selected_year}-{selected_month:02d}-{workday:02d}"

                arrival_time = "00:00"
                leave_time = "00:00"

                cursor.execute('''
                    UPDATE dochazka
                    SET arrival_time = ?, leave_time = ?
                    WHERE employee_id = ? AND date = ?
                ''', (arrival_time, leave_time, employee_id, current_date))

                if cursor.rowcount == 0:
                    cursor.execute('''
                        INSERT INTO dochazka (employee_id, date, arrival_time, leave_time)
                        VALUES (?, ?, ?, ?)
                    ''', (employee_id, date, arrival_time, leave_time))

    conn.commit()
    conn.close()


def combine_data():

    global selected_year, selected_month

    available_times = ["05:40", "13:40", "21:40"]
    selected_time = ""           
    
    
    conn_dochazka = sqlite3.connect('dochazka.db')
    cursor_dochazka = conn_dochazka.cursor()

    # Získání údajů z databáze
    cursor_dochazka.execute('''
        SELECT employee_id, date, arrival_time, leave_time
        FROM dochazka
    ''')
    records = cursor_dochazka.fetchall()

    conn_month_attendance = sqlite3.connect('MonthAttendance.db')
    cursor_month_attendance = conn_month_attendance.cursor()

    cursor_month_attendance.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            employee_name TEXT,
            date DATE,
            arrival_time TIME,
            leave_time TIME,
            CONSTRAINT unique_employee_date UNIQUE (employee_id, date)
        )
    ''')

    import json
    with open('employees.json', 'r') as file:
        employees = json.load(file)

    processed_employee_dates = set()

    for record in records:
        actual_day = None
        employee_id = str(record[0])
        date, arrival_time, leave_time = record[1:]
        if employee_id in employees:
            employee_name = employees[employee_id]

            formatted_date = datetime.strptime(date, "%Y-%m-%d")

            if (employee_id, formatted_date) not in processed_employee_dates and formatted_date.weekday() < 5:
                #print(formatted_date)
                actual_day = formatted_date.day
                #print(actual_day)
                #print(f"Employee ID: {employee_id}, Date: {date}, Day of Month: {actual_day}")

                processed_employee_dates.add((employee_id, formatted_date))
            
                employee_id = int(employee_id)        
                if employee_id is not None:                                                   
                    if 1 <= actual_day <= 7:
                        if 1000 < employee_id <= 1003:
                            selected_time = available_times[0]
                        elif 1003 < employee_id <= 1006: 
                            selected_time = available_times[1]
                        elif 1006 < employee_id <= 1009:
                            selected_time = available_times[2]
                        else:
                            selected_time = available_times[0]   
                        

                    elif 8 <= actual_day <= 14:
                        if 1000 < employee_id <= 1003:
                            selected_time = available_times[1]
                        elif 1003 < employee_id <= 1006: 
                            selected_time = available_times[2]
                        elif 1006 < employee_id <= 1009:
                            selected_time = available_times[0]
                        else:
                            selected_time = available_times[1]
                        

                    elif 15 <= actual_day <= 21:
                        if 1000 < employee_id <= 1003:
                            selected_time = available_times[2]
                        elif 1003 < employee_id <= 1006: 
                            selected_time = available_times[0]
                        elif 1006 < employee_id <= 1009:
                            selected_time = available_times[1]
                        else:
                            selected_time = available_times[2]
                        

                    elif 22 <= actual_day:
                        if 1000 < employee_id <= 1003:
                            selected_time = available_times[0]
                        elif 1003 < employee_id <= 1006: 
                            selected_time = available_times[1]
                        elif 1006 < employee_id <= 1009:
                            selected_time = available_times[2]
                        else:
                            selected_time = available_times[0]
                       
            
                    random_minutes = random.randint(0, 25)
                    random_datetime = datetime.strptime(selected_time, "%H:%M") + timedelta(minutes=random_minutes)
                    arrival_time = random_datetime.strftime(f"{selected_year}-{selected_month:02d}-{actual_day:02d} %H:%M")    

                    random_minutes1 = random.randint(-5, 10)

                    if selected_time == available_times[2]:
                        actual_day += 1
                        leave_time = (random_datetime + timedelta(hours=8, minutes=random_minutes1)).strftime(f"{selected_year}-{selected_month:02d}-{actual_day:02d} %H:%M")
                        
                        if actual_day > calendar.monthrange(selected_year, selected_month)[1]:
                            
                            if selected_month == 12:
                                selected_year += 1
                                selected_month = 1
                                actual_day = 1
                                leave_time = (random_datetime + timedelta(hours=8, minutes=random_minutes1)).strftime(f"{selected_year}-{selected_month:02d}-{actual_day:02d} %H:%M")
                            else:
                                selected_month += 1
                                actual_day = 1
                                leave_time = (random_datetime + timedelta(hours=8, minutes=random_minutes1)).strftime(f"{selected_year}-{selected_month:02d}-{actual_day:02d} %H:%M")

                        
                    else:
                        leave_time = (random_datetime + timedelta(hours=8, minutes=random_minutes1)).strftime(f"{selected_year}-{selected_month:02d}-{actual_day:02d} %H:%M")
                                                            

                    cursor_month_attendance.execute('''
                    INSERT OR IGNORE INTO attendance (employee_id, employee_name, date, arrival_time, leave_time)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (employee_id, employee_name, date, arrival_time, leave_time))            

                    cursor_month_attendance.execute('''
                        UPDATE attendance
                        SET arrival_time = ?, leave_time = ?
                        WHERE employee_id = ? AND date = ?
                    ''', (arrival_time, leave_time, employee_id, date))

    #print(selected_time, "test")

    conn_month_attendance.commit()
    conn_month_attendance.close()
    conn_dochazka.close()




