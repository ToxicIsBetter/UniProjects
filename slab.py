def rerun(fun):
     
    val = input("Do you want to run the Program again? (y/n): ").lower()
    while val != "y" and val != "n":
        val = input("Please Enter a valid value! Do you want to run the Program again? (y/n)").lower()
    # asking if the user wants to run the program again.
    while val =="y":
        fun()
        val = input("Do you want to run the Program again? (y/n): ").lower()

    if val == "n":
        print("Thank You for using the program. :)")
        print()

def validator(var):

        try:
            var = float(var)
            return True, var

        except ValueError:
            return False, None


