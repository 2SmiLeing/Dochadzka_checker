import random
import calendar
import json

def start_times():
    from workdays import selected_year, selected_month, day
    
    available_times = ["05:40", "13:40", "21:40"]
    selected_time = ""

    with open('employees.json', 'r') as file:
        employees = json.load(file)
    
    for key in employees:
        employee_id = key
        
        if employee_id is not None:
            if 0 <= calendar.weekday(selected_year, selected_month, day) <= 4:
                if 1 <= day <=7:
                    if 1001 <= int(employee_id) <= 1004:
                        selected_time = available_times[0]
                    elif 1005 <= int(employee_id) <= 1008:
                        selected_time = available_times[1]
                    elif 1009 <= int(employee_id) <= 1013:
                        selected_time = available_times[2]

                elif 8 <= day <=14:
                    if 1001 <= int(employee_id) <= 1004:
                        selected_time = available_times[1]
                    elif 1005 <= int(employee_id) <= 1008:
                        selected_time = available_times[2]
                    elif 1009 <= int(employee_id) <= 1013:
                        selected_time = available_times[0]

                elif 15 <= day <=21:
                    if 1001 <= int(employee_id) <= 1004:
                        selected_time = available_times[2]
                    elif 1005 <= int(employee_id) <= 1008:
                        selected_time = available_times[0]
                    elif 1009 <= int(employee_id) <= 1013:
                        selected_time = available_times[1]
                else:
                    selected_time = available_times[0]

    return selected_time
