print("\n")

#defininf a funciton called conv)function

def validator(var):

        try:
            var = float(var)
            return True, var

        except ValueError:
            return False, None

def conv_function():
    
    #defining the usd value

    print("\n")
    usd  = float(0.7633587786259542)

    #explaining the current rate and statring th eprogram for the user.

    print("Currency Conversion Program "+ "\n")
    print("Current Rate of GBP: 1 USD =", usd,"GBP")

    #asking user input for teh usd value

    amt = input("Enter the amount in USD you would like to convert: ")

    is_valid, amt = validator(amt);
        
    while not is_valid:
        amt = input("Invalid Input! Enter the numeric amount in USD you would like to convert: ")
        is_valid, amt = validator(amt);
        


    #converting the amount from usd to GBP

    gbp = usd*amt

    #print the usd value

    print("\n")
    print(amt, "USD is equal to",gbp,"GBP")
    print("\n")

def rerun():
     
    val = input("Do you want to run the Program again? (y/n): ").lower()
    while val != "y" and val != "n":
            val = input("Please Enter a valid value! Do you want to run the Program again? (y/n)").lower()
    # asking if the user wants to run the program again.
    while val =="y":
        conv_function()
        val = input("Do you want to run the Program again? (y/n): ").lower()

    if val == "n":
        print("Thank You for using the program. :)")
        print()


#calling the conv_function.
conv_function()

rerun();


    
    
       