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
        generated_hours.append(hours)

        for employee_id, employee_name in employees.items():
            date = f"{selected_year}-{selected_month:02d}-{workday:02d}"
            hours.random_time()
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

def combine_data():
    conn = sqlite3.connect('dochazka.db')
    cursor = conn.cursor()

    # Získání údajů z databáze
    cursor.execute('''
        SELECT employee_id, date, arrival_time, leave_time
        FROM dochazka
    ''')
    records = cursor.fetchall()

    # Načtení zaměstnanců ze souboru
    employees = load_employees()
    #print("Loaded employees:", employees)

    # Spojení údajů z JSON a databáze pomocí ID zaměstnance
    for record in records:
        employee_id = str(record[0])  # Převést employee_id na řetězec
        date, arrival_time, leave_time = record[1:]
        if employee_id in employees:
            employee_name = employees[employee_id]
            print(f"Employee: {employee_name}, Date: {date}, Arrival Time: {arrival_time}, Leave Time: {leave_time}")

    conn.close()
