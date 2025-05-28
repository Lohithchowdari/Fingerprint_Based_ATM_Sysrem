# importing libr
# aries
import os 
import time as t

#importing modules 
import registration_module as rm
import transaction_module as tm
from login_module import login

def second_menu(acc_no, name):
    print("Hi ", name)
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Mini Statement")
    print("4. Exit")
    choice_second = int(input("Choose any option....... \n"))
    if choice_second == 1:
        tm.Withdraw(acc_no)
    elif choice_second == 2:
        tm.Deposit(acc_no)
    elif choice_second == 3:
        tm.Mini_statement(acc_no)
    elif choice_second == 4:
        exit("Thanks for using XYZ Bank")
    else:
        print("You have chosen the wrong option....")
        second_menu(acc_no, name)


while True:
    os.system("cls")
    print("WELCOME".center(50, "*"))
    print("1. Registration")
    print("2. Login       ")
    choice_first = int(input("Choose Any Option : "))
    if choice_first == 1:
        rm.registeration()
    elif choice_first == 2:
        login_result = login()
        if login_result:
            result, acc_no, login_first_name = login_result
            if result:
                second_menu(acc_no, login_first_name)
        else:
            print("⚠️ Login failed. Please try again.")
            t.sleep(3)
    else:
        print("You have choosed the wrong option...")
        print("Please select the correct option")
        t.sleep(3)
