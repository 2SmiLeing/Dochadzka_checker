from employees import *
import random
import calendar

def input_year():
    while True:
        year_input = input("Input Year: ")
        if len(year_input) != 4 or not year_input.isdigit():
            print("Invalid input. Year must be a four-digit integer.")
        else:
            return int(year_input)

def input_month():
    while True:
        month_input = input("Input Month: ")
        if not month_input.isdigit() or not 1 <= int(month_input) <= 12:
            print("Invalid input. Month must be a two-digit integer 1-12")
        else:
            return int(month_input)

selected_year = input_year()
selected_month = input_month()

_, days_in_month = calendar.monthrange(selected_year, selected_month)
workdays_count = 0

for day in range(1, days_in_month + 1):
    weekday = calendar.weekday(selected_year, selected_month, day)
    if 0 <= weekday <= 4:
        workdays_count += 1

print(f"V mesiaci {selected_year}-{selected_month} je {workdays_count} pracovních dní.")
