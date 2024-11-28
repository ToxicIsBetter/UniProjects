# file = open("Employee.txt", "r")
# print(file.read())
# file.close()

emp = []

with open("Employee.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        emp.append(data)

first_name = 0
surname = 1
gender = 2
rank = 3
type = 4
basic_salary = 5
hours_worked = 6

for employee in emp[1:]:
    try:
        employee[basic_salary] = float(employee[basic_salary])
        employee[hours_worked] = int(employee[hours_worked])
    except: 
        ValueError

print()
for row in emp:
    print(row)   
print()     

def hre_basic() -> dict:
    temp_dict = {}
    index = 1

    for employee in emp[1:]:
        if employee[type] == 'hourly':
            emp_salary = employee[basic_salary] * employee[hours_worked] 
        else:
            emp_salary = -1
        temp_dict[index] = emp_salary
        index += 1
    return temp_dict

emp_sal = hre_basic()
emp_sal = {key: value for key, value in sorted(emp_sal.items()) if value != -1}

print()
for key, value in emp_sal.items():
    print(f"Employee Index {key}: {value}")
print()


def calculate_bonus(emp_index: int, bonus_percentage) -> float:
    if emp_index in emp_sal.keys():
        salary = float(emp_sal[emp_index])
    else:
        salary = float(emp[emp_index][basic_salary])

    bonus = float(salary * bonus_percentage)
    total_salary = bonus + salary
    return total_salary
print()
for employee in emp[1:]:
        
    if employee[rank] == 'officer':
        bonus_percentage = 0.20
    else:
        bonus_percentage = 0.15

    total_salary = calculate_bonus(emp.index(employee), bonus_percentage)
    # Print the bonus for each employee
    print(f"Total_Salary after bonus for {employee[first_name]} {employee[surname]}: {total_salary}")     
print()
