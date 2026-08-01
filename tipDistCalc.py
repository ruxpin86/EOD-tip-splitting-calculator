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


def calculate_tip_share(employee_info, total_tips):
    total_hours = sum(employee_info.values())

    if total_hours == 0:
        return {}, 0

    tips_per_hour = total_tips / total_hours

    payouts = {}
    for name, hours in employee_info.items():
        ind_empl_total = hours * tips_per_hour
        payouts[name] = {
            "tips": ind_empl_total,
            "hours": hours
        }

    return payouts, tips_per_hour

def main():
    emp_info = get_employee_info()
    calculate_tip_share(emp_info)

if __name__ == "__main__":
    main()