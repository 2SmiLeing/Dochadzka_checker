import random
import calendar

available_times = ["05:40", "13:40", "21:40"]
selected_time = ""
n = 0

if 0 <= calendar.weekday(year, month, day) <= 4:
    if day in range(1, 7):
        selected_time = available_times[n]
    elif day in range(7, 15):
        selected_time = available_times[n+1]
    elif day in range(15,22):
        selected_time = available_times[n+2]
    else:
        selected_time = available_times[n]
