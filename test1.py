import random
import calendar
import sqlite3

available_times = ["05:40", "13:40", "21:40"]
selected_time = ""
n = [[0, 1, 2], [1,2,0], [2,0,1]]

conn_dochazka = sqlite3.connect('dochazka.db')
cursor_dochazka = conn_dochazka.cursor()

cursor_dochazka.execute('''
        SELECT employee_id
        FROM dochazka
    ''')

records = cursor_dochazka.fetchall()

employee_id = int(records[0])
        
if employee_id 

if 0 <= calendar.weekday(year, month, day) <= 4:
    if day in range(1, 7):
        selected_time = available_times[n[x][0]]
    elif day in range(7, 15):
        selected_time = available_times[n[y][1]]
    elif day in range(15,22):
        selected_time = available_times[n[z][2]]
    else:
        selected_time = available_times[n[x][0]]
