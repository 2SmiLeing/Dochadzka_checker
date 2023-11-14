import sqlite3
from employees import *
from workdays import workdays_count
from time_arrival_leave import *

def databaze():
    # Vytvoření nebo připojení k databázi
    conn = sqlite3.connect('dochazka.db')
    cursor = conn.cursor()

    # Vytvoření tabulky pro docházku, pokud neexistuje
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dochazka (
            id INTEGER PRIMARY KEY,
            employee_id INTEGER,
            date DATE,
            arrival_time TIME,
            leave_time TIME
        )
    ''')

    # Přidání nebo aktualizace záznamů o docházce
    for workday in range(1, workdays_count + 1):
        hours = HoursAtWork(selected_year, selected_month, workday, "", "")
        hours.random_time()
        generated_hours.append(hours)

        for employee_id, employee_name in employees.items():
            date = f"{selected_year}-{selected_month:02d}-{workday:02d}"
            arrival_time = hours.time_arrival
            leave_time = hours.time_leave

            # Aktualizace záznamu, pokud existuje, jinak vložení nového
            cursor.execute('''
                UPDATE dochazka
                SET arrival_time = ?, leave_time = ?
                WHERE employee_id = ? AND date = ?
            ''', (arrival_time, leave_time, employee_id, date))

            if cursor.rowcount == 0:
                # Žádný záznam nebyl aktualizován, takže vložíme nový
                cursor.execute('''
                    INSERT INTO dochazka (employee_id, date, arrival_time, leave_time)
                    VALUES (?, ?, ?, ?)
                ''', (employee_id, date, arrival_time, leave_time))

    # Uložení změn a uzavření spojení s databází
    conn.commit()
    conn.close()
