import math

def get_employee_info():
    num_employees = int(input("Enter number of employees on tip pool: "))
    employee_dict = {}

    for _ in range(num_employees):
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

    print(f"Total tips: S{total_tips:.2f}")
    print(f"Hours on tip pool: {total_hours}")
    print(f"Tips per hour: ${tips_per_hour:.2f}")

    for key in employee_info:
        hours = employee_info[key]
        ind_empl_total = hours * tips_per_hour
        employee_info[key] = ind_empl_total

    print(f"Employee individual payout: {employee_info}")

    return employee_info


def main():
    emp_info = get_employee_info()
    calculate_tip_share(emp_info)

if __name__ == "__main__":
    main()