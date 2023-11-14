import sqlite3

# Připojení k databázi
conn = sqlite3.connect('dochazka.db')
cursor = conn.cursor()

# Výběr všech dat z tabulky "dochazka"
cursor.execute("SELECT * FROM dochazka")
rows = cursor.fetchall()

# Vypsání dat
for row in rows:
    print(row)

# Uzavření spojení
conn.close()