import time
import mysql.connector 
import os
import datetime
conn = mysql.connector.connect(
    user='root',
    password='KLaftEEZoBvrSelyDyFsQXrgkjYLdmZA',
    host='crossover.proxy.rlwy.net',
    port=26866,
    database='railway',
    autocommit=True
)
connection_cursor = conn.cursor()
def Withdraw(acc_no):
    os.system("cls")
    amt = int(input("Enter the amount you want to withdraw : "))
    select_balance_sql_query = """select Balance from ATM_database where Account_no = %s"""
    connection_cursor.execute(select_balance_sql_query,(acc_no,))
    queryResult = connection_cursor.fetchall()
    balance = queryResult[0][0]

    if balance <amt :
        print("You did not have that much balance ")
        time.sleep(2)
        Withdraw(acc_no)
    balance -= amt
    current_time = datetime.datetime.now()
    trans = "Debited"
    update_balance_sql_query = """update ATM_database set Balance = %s, Transaction = %s, Amount = %s,  Date_Time = %s where Account_no = %s"""
    update_balance_sql_tuple = (balance,trans,amt,current_time,acc_no)
    connection_cursor.execute(update_balance_sql_query,update_balance_sql_tuple)
    print("Your money has been successfully withdrawal")
    exit()
    
def Deposit(acc_no):
    os.system("cls")
    amt = int(input("Enter the amount you want to deposit : "))
    select_balance_sql_query = """select Balance from ATM_database where Account_no = %s"""
    connection_cursor.execute(select_balance_sql_query,(acc_no,))
    queryResult = connection_cursor.fetchall()
    balance = queryResult[0][0]
    balance += amt
    current_time = datetime.datetime.now()
    trans = "Credited"
    update_balance_sql_query = """update ATM_database set Balance = %s, Transaction = %s, Amount = %s, Date_Time = %s where Account_no = %s"""
    update_balance_sql_tuple = (balance,trans,amt,current_time,acc_no)
    connection_cursor.execute(update_balance_sql_query,update_balance_sql_tuple)
    print("Your money has been successfully deposited")
    exit()
    

def Mini_statement(acc_no):
    os.system("cls")
    mini_statement_sql_query = """select * from transaction_sheet where Account_no = %s"""
    connection_cursor.execute(mini_statement_sql_query,(acc_no,))
    mini_statement_search_result = connection_cursor.fetchall()
    for row in  mini_statement_search_result:
        print("Account_no :",row[0])
        print("Current Balance :",row[1])
        print("Last Transaction Status :",row[2])
        print("Last Transaction Amount :",row[3])
        print("Last Transaction Date and Time :",row[4])
        exit()