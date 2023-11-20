import sqlite3

# Připojení k databázi
conn = sqlite3.connect('MonthAttendance.db')
cursor = conn.cursor()

# Výběr všech dat z tabulky "dochazka"
cursor.execute("SELECT * FROM attendance")
rows = cursor.fetchall()

# Vypsání dat
for row in rows:
    print(row)

# Uzavření spojení
conn.close()
