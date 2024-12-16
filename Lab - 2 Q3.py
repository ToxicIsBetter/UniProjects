#defininng a function called exam.
def validator(var):

        try:
            var = float(var)
            if var > 0 and var < 100:     
                return True, var
            else:
                return False, None

        except ValueError:
            return False, None

def exam(mark, name):
    is_valid = 0    
    #using if else to validate which mark corresponds to which grade.
    is_valid, mark = validator(mark);
        
    while is_valid == False:
        mark = input("Invalid Input! Enter the numeric value between 1 and 100: ")
        is_valid, mark = validator(mark);



    if mark >= 70:
        print(mark, "marks is 'A' Grade for the module", name)

    elif 60 <= mark and mark < 70:
        print(mark, "marks is 'B' Grade for the module", name)

    elif 50 <= mark and mark < 60:
        print(mark, "marks is 'C' Grade for the module", name)

    elif 40 <= mark and mark < 50:
        print(mark, "marks is 'D' Grade for the module", name)

    else:
        print(mark, "marks is 'F' Grade for the module", name)


#defining another function called validator to validate the input of the marks

def rerun(mark, name):
     
    val = input("Do you want to run the Program again? (y/n): ").lower()
    while val != "y" and val != "n":
            val = input("Please Enter a valid value! Do you want to run the Program again? (y/n)").lower()
    # asking if the user wants to run the program again.
    while val =="y":   
        mod_name = input("Enter the name of the module: ")
        mod_mark = input("Enter the mark received: ")
        exam(mark, name);
        val = input("Do you want to run the Program again? (y/n): ").lower()

    if val == "n":
        print("Thank You for using the program. :)")
        print()

"""
asking the user for input of marks
and for the input of module name
"""

name = input("Enter the name of the module: ")
mark = input("Enter the mark received: ")
    
#calling the exam function with the marks valuye in to output the grade.
exam(mark, name);
rerun(mark, name);