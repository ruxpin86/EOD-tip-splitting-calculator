import math

def get_employee_info():
    num_employees = int(input("Enter number of employees on tip pool: "))
    employee_dict = {}

    for i in range(num_employees):
        employee = input("Enter employee NAME: ")
        hours = int(input("Enter employee HOURS on tip pool: "))
        employee_dict[employee] = hours
        
    print(f"Employee hours dictionary: {employee_dict}")
    return employee_dict


def calculate_tip_share(employee_info):
    total_tips = float(input("What was the total amount of tips collected?: "))
    employee_hours = []
    for key in employee_info:
        hours = employee_info[key]
        employee_hours.append(hours)
    total_hours = sum(employee_hours)

    tips_per_hour = total_tips / total_hours

    print(f"Tips per hour: ${tips_per_hour:.2f}")

def main():
    emp_info = get_employee_info()
    calculate_tip_share(emp_info)

if __name__ == "__main__":
    main()