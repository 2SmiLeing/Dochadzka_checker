import json
import time

def print_with_delay(text, delay=0.02):
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)

#Save dict. employees:
def save_employees(data):
    with open('employees.json', 'w') as file:
        json.dump(data, file)

def load_employees():
    try:
        with open('employees.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

employees = load_employees()

#Add new employee:
def new_employee():
    name = input('Vlozte Mena zamestnancov. \nPre ukoncenie zadajte "Koniec". \n\nZadajte meno zamestnanca: ').title()
    print("\n")
    print_with_delay("\n-------------------------------------------\n", 0.01)
    # Clear dict. employees:
    if name.lower() == "delete":
        global employees
        employees = {}
        save_employees(employees)
        print_with_delay("Employees cleared.")
        print("\n")
        new_employee()
    #Terminate running terminal:
    elif name.lower() == "koniec":
        print_with_delay("Program terminated.")
        print("\n")
        print(employees)
        print("\n")
        return 
    else:
        #Check dict. employees:
        if employees:
            new_key = str(max(map(int, employees.keys())) + 1)
        else:
            #New emoloyee:
            new_key = 1001
        employees[new_key] = name
        print_with_delay(f"Novy zamestnanec pridany s ID: {new_key}.")
        print("\n")
        save_employees(employees)
        print(employees)
        print("\n")
        new_employee()



