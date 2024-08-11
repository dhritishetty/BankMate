import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='BankPro')
mycursor = mydb.cursor(buffered=True)

def Menu():
    print('*' * 124)
    print("MAIN MENU")
    print('1. Insert Records')
    print('2. Display all the records as per account number')
    print('3. Search record details as per Account Number')
    print('4. Update Record')
    print('5. Delete Record')
    print('6. Transaction debit/withdraw from the Account')
    print('7. Credit into the account')
    print('8. Exit')
    print('*' * 124)

def Insert():
    while True:
        acc = int(input('Enter account number:'))
        name = input('Enter Name')
        mob = int(input('Enter Mobile number'))
        email = input("Enter email")
        add = input('Enter Address')
        city = input("Enter city")
        bal = float(input('Enter Balance'))
        rec = [acc, name.upper(), mob, email, add, city.upper(), bal]
        cmd = "Insert into bank values(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(cmd, rec)
        mydb.commit()
        ch = input("more? (Y/N): ")
        if ch.lower() == 'n':
            break

def Retrieve_All():
    mycursor.execute('Select * from bank')
    t = "%15s %15s %15s %15s %15s %15s %15s"
    print(t % ('Account No', 'Name', 'Mobile Number', 'Email', 'Address', 'City', 'Balance'))
    for i in mycursor:
        print(t % (i))

def Search_Acc():
    mycursor.execute('Select * from bank')
    acc = int(input("Enter the account number to be searched: "))
    t = "%15s %15s %15s %15s %15s %15s %15s"
    for i in mycursor:
        if i[0] == acc:
            print(t % ('Account No', 'Name', 'Mobile Number', 'Email', 'Address', 'City', 'Balance'))
            for j in i:
                print('%15s' % (j), end=" ")

def Update():
    mycursor.execute('Select * from bank')
    acc = int(input("Enter the account number to be changed: "))
    for i in mycursor:
        i = list(i)
        if i[0] == acc:
            ch = input('Change Name (Y/N): ')
            if ch.lower() == 'y':
                i[1] = input('Enter Name').upper()
            ch = input('Change Mobile Number (Y/N): ')
            if ch.lower() == 'y':
                i[2] = int(input('Enter Mobile Number'))
            ch = input('Change Email (Y/N): ')
            if ch.lower() == 'y':
                i[3] = input('Enter Email')
            ch = input('Change Address (Y/N): ')
            if ch.lower() == 'y':
                i[4] = input('Enter Address')
            ch = input('Change City (Y/N): ')
            if ch.lower() == 'y':
                i[5] = input('Enter City').upper()
            ch = input('Change Balance (Y/N): ')
            if ch.lower() == 'y':
                i[6] = float(input('Enter Balance'))
            cmd = 'update bank set name=%s, mobile=%s, email=%s, address=%s, city=%s, balance=%s where accno=%s'
            val = (i[1], i[2], i[3], i[4], i[5], i[6], i[0])
            mycursor.execute(cmd, val)
            mydb.commit()
            print('Value Updated')
            break

def Delete():
    mycursor.execute('Select * from bank')
    acc = int(input("Enter the account number to be deleted: "))
    for i in mycursor:
        i = list(i)
        if i[0] == acc:
            cmd = 'delete from bank where accno = %s'
            val = (i[0],)
            mycursor.execute(cmd, val)
            mydb.commit()
            print('Value Deleted')
            break
        else:
            print('Value not present')

def Debit():
    mycursor.execute('Select * from bank')
    print('Please maintain minimum balance Rs3000')
    acc = int(input("Enter the account number from which money is to be debited: "))
    for i in mycursor:
        i = list(i)
        if i[0] == acc:
            amt = int(input("Enter the amount to be debited: "))
            if (i[6] - amt) > 3000:
                i[6] -= amt
                cmd = "update bank set balance=%s where accno=%s"
                val = (i[6], i[0])
                mycursor.execute(cmd, val)
                mydb.commit()
                print('Amount Debited')
            else:
                print('Insufficient Balance')
            break

def Credit():
    mycursor.execute('Select * from bank')
    acc = int(input("Enter the account number to be credited: "))
    for i in mycursor:
        i = list(i)
        if i[0] == acc:
            amt = int(input("Enter the amount to be credited: "))
            i[6] += amt
            cmd = "update bank set balance=%s where accno=%s"
            val = (i[6], i[0])
            mycursor.execute(cmd, val)
            mydb.commit()
            print('Amount Credited')
        else:
            print('Record not found')
            break

while True:
    Menu()
    ch = int(input('Select any one between 1 to 8: '))
    if ch == 1:
        Insert()
    elif ch == 2:
        Retrieve_All()
    elif ch == 3:
        Search_Acc()
    elif ch == 4:
        Update()
    elif ch == 5:
        Delete()
    elif ch == 6:
        Debit()
    elif ch == 7:
        Credit()
    elif ch == 8:
        break
    else:
        print('Invalid Selection')
        break
