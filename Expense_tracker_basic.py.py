# EXPENSE TRACKER
from datetime import datetime

expense_sheet= []

while True:
    print("===== OPTIONS =====")
    print("1. ADD Expenses")
    print("2. View All expenses")
    print("3. View ")
    print("4. None/Exit ")

    choice = int(input("Enter options from the above:- "))

# When user chooses option 1

    if (choice == 1):
        date = input("Enter the date (DD/MM/YYYY): ")     

        category = input("Enter category of expense :- ")

        description = input("Decribe expense:- ")
        amount = float(input("Enter amount: "))

        expense = {
            "DATE": date,
            "CATEGORY" : category,
            "ITEMS" : description,
            "AMOUNT" : amount
        }

        expense_sheet.append(expense)
        print(" \n ")
        print("--------------Expense is added --------------" )
        print(expense_sheet)

# when user chooces option 2

    elif (choice == 2):
        if (len(expense_sheet) == 0):
            print("No expenses till date \n ADD EXPENSES")

        else:
            print("----------- Here is your expenses ----------")
            count = 1
            for bills in expense_sheet:
                print(f"BILL number:{count} \n {bills["date"]},{bills["CATEGORY"]},{bills["ITEMS"]},{bills["AMOUNT"]}")
                count +=1

# When user chooses option 3

    elif (choice==3) :
        total = 0
        for Bill in expense_sheet:
            total += Bill["AMOUNT"] 

        print(" \n TOTAL EXPENSES  is :- ",total)

    elif (choice == 4):
        print(" THANKS FOR USING OUR SYSTEM \nHOPE YOU LIKED IT !")
        break

    else:
        print("Enter a valid option")
