"""Employee Salary Analyzer."""

def calculate_total_payroll(salaries):
    """Calculate total payroll without using sum()."""
    total = 0
    for salary in salaries:
        total += salary
    return total


def calculate_average_salary(salaries):
    """Calculate average employee salary."""
    return calculate_total_payroll(salaries) / len(salaries)


def find_highest_salary(salaries):
    """Find the highest salary manually."""
    highest = salaries[0]
    for salary in salaries:
        if salary > highest:
            highest = salary
    return highest


def find_lowest_salary(salaries):
    """Find the lowest salary manually."""
    lowest = salaries[0]
    for salary in salaries:
        if salary < lowest:
            lowest = salary
    return lowest


def employees_above_average(salaries, average):
    """Return salaries that are above the average."""
    above_average = []
    for salary in salaries:
        if salary > average:
            above_average.append(salary)
    return above_average


def main():
    """Run the employee salary analyzer."""
    print("===== EMPLOYEE SALARY ANALYZER =====")
    while True:
        try:
            count = int(input("Enter number of employees: "))
            if count > 0:
                break
            print("Enter at least one employee.")
        except ValueError:
            print("Please enter a whole number.")

    salaries = []
    for index in range(1, count + 1):
        while True:
            try:
                salary = float(input(f"Enter salary for employee {index}: "))
                if salary >= 0:
                    salaries.append(salary)
                    break
                print("Salary cannot be negative.")
            except ValueError:
                print("Please enter a valid salary.")

    total = calculate_total_payroll(salaries)
    average = calculate_average_salary(salaries)
    highest = find_highest_salary(salaries)
    lowest = find_lowest_salary(salaries)
    above_average = employees_above_average(salaries, average)

    print("\n===== SALARY ANALYSIS =====")
    print(f"Total payroll: {total:.2f}")
    print(f"Average salary: {average:.2f}")
    print(f"Highest salary: {highest:.2f}")
    print(f"Lowest salary: {lowest:.2f}")
    print("Employees earning above average:")
    if above_average:
        for salary in above_average:
            print(f"- {salary:.2f}")
    else:
        print("None")


if __name__ == "__main__":
    main()
