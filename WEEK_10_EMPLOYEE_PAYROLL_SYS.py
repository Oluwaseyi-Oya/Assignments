# EMPLOYEE PAYROLL SYSTEM
# Build a payroll system where employees' details such as salary, position, and bonuses are stored.
# Dictionary of dictionaries, where the outer dictionary holds employee names and the inner dictionary
# contains details like salary, position, and bonuses.
# Add or update employee details.
# Calculate monthly salary (with bonuses).

employee_payroll = {}


def add_employee(name, position, salary,  **kwargs):
    """
    adds an employee to the employee payroll

    parameter:
    name(str): name of employee to be added
    position(str): position the employee holds
    salary(int): salary of the employee
    kwargs: a dict for more info on the employee bonus type if any

    returns
    none
    """

    employee_payroll[name] = {'position': position, 'salary': salary, 'bonuses': {}}

    for key, value in kwargs.items():
        employee_payroll[name]['bonuses'] = value
    print (f"{name} added successfully!")

def add_update_employee(name, position, salary, **kwargs):
    """
        adds an employee to the employee payroll if it hasn't been added befor

        parameter:
        name(str): name of employee to be added
        position(str): position the employee holds
        salary(int): salary of the employee
        kwargs: a dict for more info on the employee bonus type if any

        returns
        none
        """

    employee = employee_payroll.get(name)
    if employee is None:
        print (f"{name} isn't on the employee payroll!")
        add_employee(name, position, salary, **kwargs)
    else:
        employee['position'] = position
        employee['salary'] = salary
        employee['bonuses'].update(kwargs.get('bonuses', {}))

def monthly_salary_bonuses(name):
    """
        calculates the monthly salary of an employee including the bonuses if any

        parameter:
        name(str): name of employee whose monthly salary is to be calculated

        returns
        none
        """
    employee = employee_payroll.get(name)


    if employee is None:
        print (f"Cannot find student: {name}")
    else:
        salary = employee.get('salary')
        bonuses = employee.get('bonuses')
        if bonuses:
            monthly_salary = salary + bonuses
            print (monthly_salary)
        else:
            print(salary)
            # print(name)
            # print(employee)
            # print(monthly_salary)



add_employee("Mahmud", "Data Scientist", 150000, sign_on = 5000)
add_update_employee("Suzanna", "Receptionist", 60000, annual = 1500)
add_employee("Olamide", "Lead Scientist", 200000)
add_employee("Ajara", "Project Manager", 10000)
#print(employee_payroll)
#monthly_salary_bonuses("Mahmud")

