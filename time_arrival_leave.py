import datetime
import random
from workdays import selected_year, selected_month
import calendar

year = selected_year
month = selected_month

class HoursAtWork:
    def __init__(self, year, month, day, time_arrival, time_leave):
        self.year = year
        self.month = month
        self.day = day        
        self.time_arrival = time_arrival
        self.time_leave = time_leave
        
    def random_time(self):    
        available_times = ["05:40", "13:40", "21:40"]
        selected_time = random.choice(available_times)
        random_minutes = random.randint(0, 25)
        random_datetime = datetime.datetime.strptime(selected_time, "%H:%M") + datetime.timedelta(minutes=random_minutes)
        
        self.time_arrival = random_datetime.strftime(f"{year}:{month}:{self.day}:%H:%M")
        
        random_minutes1 = random.randint(-5, 10)
        
        self.time_leave = (random_datetime + datetime.timedelta(hours=8, minutes=random_minutes1)).strftime(f"{year}:{month}:{self.day}:%H:%M")

# Získání všech pracovních dní v měsíci
_, days_in_month = calendar.monthrange(year, month)
workdays = [day for day in range(1, days_in_month + 1) if 0 <= calendar.weekday(year, month, day) <= 4]

# Vytvoření a vygenerování hodin pro každý pracovní den
generated_hours = []
for workday in workdays:
    hours = HoursAtWork(year, month, workday, "", "")
    hours.random_time()
    generated_hours.append(hours)

# Tisk vygenerovaných hodin
#for hours in generated_hours:
#    print(f"Arrival time: {hours.time_arrival}")
#    print(f"Leave time: {hours.time_leave}")
#   print()
