import os
import time
import mysql.connector 
from tkinter import Tk     
from tkinter.filedialog import askopenfilename
import binary_processing_module as bmp
import ATM_authentication as auth

conn = mysql.connector.connect(
    user='root',
    password='KLaftEEZoBvrSelyDyFsQXrgkjYLdmZA',
    host='crossover.proxy.rlwy.net',
    port=26866,
    database='railway',
    autocommit=True
)
connection_cursor = conn.cursor()




def login():
    os.system("cls")
    print("Hey User \nWelcome to SRM Bank")
    acc_no = input("Enter your account number :")
    search_name_query = """select first_name,block_status,block_time from ATM_database where Account_no = %s """
    connection_cursor.execute(search_name_query,(acc_no,))
    searchResult = connection_cursor.fetchall()
    block = searchResult[0][1]
    blocktime = searchResult[0][2]
    trial = 0
    if len(searchResult) == 0:
        print("No Account has been registered by Account_no :",acc_no)
        exit()
    
    if block == "Blocked":
        print("Your account has been blocked on",blocktime)
        exit()

    login_first_name = searchResult[0][0]
    time.sleep(2)
    os.system("cls")
    print("Welcome {}".format(login_first_name))

    result_of_checking = auth.checking_finger_print(acc_no,trial)
    
    if result_of_checking == True:
        return True,acc_no,login_first_name
