import json

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
    name = input("Please input full Name:").title()
    # Clear dict. employees:
    if name.lower() == "delete":
        global employees
        employees = {}
        save_employees(employees)
        print("Employees cleared.")
        new_employee()
    #Terminate running terminal:
    elif name.lower() == "kill":
        print("Program terminated.")
        print(employees)
        return 
    else:
        #Check dict. employees:
        if employees:
            new_key = str(max(map(int, employees.keys())) + 1)
        else:
            #New emoloyee:
            new_key = 1001
        employees[new_key] = name
        print(f"New employee added with number {new_key}.")
        save_employees(employees)
        new_employee()
