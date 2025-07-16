from db_config import connect

def create_account():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    balance = float(input("Enter amount required to open account: "))
    db = connect()
    cursor = db.cursor()
    sql = "INSERT INTO accounts (name, email, balance) VALUES (%s, %s, %s)"
    values = (name, email, balance)
    cursor.execute(sql, values)
    db.commit()  
    print("Account Created Successfully")
    db.close()

def view_accounts():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    print("All Accounts")
    if not accounts:
        print("No accounts found.")
    else:
        for acc in accounts:
            print(f"ID: {acc[0]}, Name: {acc[1]}, Email: {acc[2]}, Balance: {acc[3]}")
    db.close()

def deposit_money():
    acc_id = int(input("Enter Account Id: "))
    amount = float(input("Enter deposit amount: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, acc_id))
    db.commit()
    print("Money Deposited Successfully")
    db.close()

def withdraw_money():
    acc_id = int(input("Enter Account Id: "))
    amount = float(input("Enter amount to withdraw: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id = %s", (acc_id,))
    result = cursor.fetchone()
    if result and result[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, acc_id))
        db.commit()
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
    db.close()

def check_balance():
    acc_id = int(input("Enter Account Id: "))
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT name, balance FROM accounts WHERE id = %s", (acc_id,))
    result = cursor.fetchone()
    if result:
        print(f"Account Holder: {result[0]}, Balance: {result[1]}")
    else:
        print("Account Not Found")
    db.close()
