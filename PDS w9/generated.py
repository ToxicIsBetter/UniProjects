import pandas as pd

# Step 1: Load and Display File Contents
with open("Employee.txt", "r") as file:
    print("File Contents:")
    print(file.read())

# Step 2: Parse File into List of Lists
emp = []
with open("Employee.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        emp.append(data)

# Step 3: Insert Hourly Rate Header for Clarity
emp[0].insert(6, 'hourly_rate')
emp[0].append('basic_salary')  # Add basic salary header

# Step 4: Index Mapping
first_name = 0
surname = 1
gender = 2
rank = 3
type_id = 4
basic_salary_id = 5
hours_worked_id = 6


# Step 5: Adding Basic Salary for Hourly Employees
def hre_basic():
    for employee in emp[1:]:  # Skip the header
        if employee[type_id] == 'hourly':
            # Convert to float for calculations
            hourly_rate = float(employee[5])
            hours_worked = float(employee[6])
            emp_salary = hourly_rate * hours_worked
            employee.append(emp_salary)  # Append calculated salary
        else:
            employee.append(employee[5])  # For monthly, retain the basic salary

hre_basic()
print("\nEmployee Data with Basic Salaries:")
for row in emp:
    print(row)
