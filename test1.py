import calendar

def input_year_month():
    while True:
        year_input = input("Zadajte rok: ")
        month_input = input("Zadajte mesiac: ")

        if len(year_input) != 4 or not year_input.isdigit() or not month_input.isdigit() or not 1 <= int(month_input) <= 12:
            print("Neplatný vstup. Rok musí byť štvorciferné celé číslo a mesiac musí byť dvojciferné celé číslo medzi 1 a 12.")
        else:
            return int(year_input), int(month_input)

def filter_data_by_name_or_id(data, name_or_id, year, month):
    filtered_data = []
    for worker_data in data:
        if str(worker_data[0]) == name_or_id or worker_data[1] == name_or_id:
            date_parts = worker_data[2].split("-")
            data_year, data_month = int(date_parts[0]), int(date_parts[1])
            if data_year == year and data_month == month:
                filtered_data.append(worker_data)
    return filtered_data

selected_year, selected_month = input_year_month()

# workers_data môže byť napríklad zoznam zamestnancov, kde každý zamestnanec je zoznam [ID, meno, dátum, príchod, odchod]
workers_data = [
    [1, "John Doe", "2023-11-22", "08:00", "17:00"],
    # ďalší zamestnanec...
]

name_or_id = input("Zadajte meno alebo ID zamestnanca: ")
filtered_data = filter_data_by_name_or_id(workers_data, name_or_id, selected_year, selected_month)

for worker_data in filtered_data:
    employee_id, employee_name = str(worker_data[0]), worker_data[1]
    date = worker_data[2]
    arrival_time_str = worker_data[3]
    leave_time_str = worker_data[4]

    # ďalej spracujte údaje podľa potreby
    print(f"ID: {employee_id}, Meno: {employee_name}, Dátum: {date}, Príchod: {arrival_time_str}, Odchod: {leave_time_str}")
