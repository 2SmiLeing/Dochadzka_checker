import random
import calendar
import json

def start_times():
    from workdays import selected_year, selected_month, day

    available_times = ["05:40", "13:40", "21:40"]
    selected_time = ""

    with open('employees.json', 'r') as file:
        employees = json.load(file)

            

    if employee_id is not None:
        if 0 <= calendar.weekday(selected_year, selected_month, day) <= 4:
            if day in range(1, 7):
                if employee_id % 2 == 0:
                    selected_time = available_times[0]
            elif day in range(7, 15):
                if employee_id % 3 == 0:
                    selected_time = available_times[1]
            elif day in range(15, 22):
                if employee_id % 5 == 0:
                    selected_time = available_times[2]
            else:
                selected_time = available_times[0]

    return selected_time
