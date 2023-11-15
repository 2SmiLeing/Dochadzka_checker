import sqlite3
from employees import *
from workdays import workdays_count
from time_arrival_leave import *
from datetime import datetime

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

    for workday in range(1, workdays_count + 1):
        # Kontrola, zda je den v pracovním týdnu (pondělí až pátek)
        current_date = datetime(selected_year, selected_month, workday)
        if current_date.weekday() < 5:
            hours = HoursAtWork(selected_year, selected_month, workday, "", "")
            generated_hours.append(hours)

            for employee_id, employee_name in employees.items():
                date = f"{selected_year}-{selected_month:02d}-{workday:02d}"
                hours.random_time()
                arrival_time = hours.time_arrival
                leave_time = hours.time_leave

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
    conn_dochazka = sqlite3.connect('dochazka.db')
    cursor_dochazka = conn_dochazka.cursor()

    # Získání údajů z databáze
    cursor_dochazka.execute('''
        SELECT employee_id, date, arrival_time, leave_time
        FROM dochazka
    ''')
    records = cursor_dochazka.fetchall()

    employees = load_employees()

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

    for record in records:
        employee_id = str(record[0])
        date, arrival_time, leave_time = record[1:]
        if employee_id in employees:
            employee_name = employees[employee_id]

            cursor_month_attendance.execute('''
                INSERT OR IGNORE INTO attendance (employee_id, employee_name, date, arrival_time, leave_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (employee_id, employee_name, date, arrival_time, leave_time))

            cursor_month_attendance.execute('''
                UPDATE attendance
                SET arrival_time = ?, leave_time = ?
                WHERE employee_id = ? AND date = ?
            ''', (arrival_time, leave_time, employee_id, date))

    conn_month_attendance.commit()
    conn_month_attendance.close()
    conn_dochazka.close()
