import os
j=0
c=0
Amount_in_atm=100000
s1=40
s2=20
s3=20
s4=60
adminlist=[]
transaction_history_list=[]
lp=[]
l1=[{'name':'Ram','password':'5678','balance':70000,'bank':'sbi','tcount':0,'withdrawan amount':0},{'name':'Raj','password':'1000','balance':60000,'bank':'axis','tcount':0,'withdrawan amount':0}]
l=[{'adminname':'Gokul','password':'1234'}]
def checkusername(z):
    global j
    for i in l:
        if((i['adminname']==z['adminname']) and (i['password']==z['password'])):
            print("Welcome",z['adminname'])
            b=i
            print(" ")
            return adminhome(b)
    else:
        os.system('cls')
        print("Username not found... Please check your username or password")
        j+=1
        if(j==3):
            print("Too many attempts...")
            print(" ")
            print("Please try later...")
        else:
            return home()

def adminhome(b):
    os.system('cls')
    print("Welcome Admin")
    print(" ")
    print("1. Amount Update")
    print("2. ATM Stock check")
    print("3. Amount update history")
    print("4. Exit")
    print(".........")
    p1=int(input("Enter your Choice: "))
    if(p1==1):
        amountupdate(b)
    elif(p1==2):
        atmstock(b)
    elif(p1==3):
        amount_update_history(b)
    elif(p1==4):
        exitid()
    else:
        print("Invalid input")

def amount_update_history(b):
    os.system('cls')
    print("Amount updated in the ATM")
    print(" ")
    for i in adminlist:
        print(i)
    print(" ")
    log=input("To logout please type 1 :")
    if(log=="1"):
        os.system('cls')
        return adminhome(b)

def amountupdate(b):
    global Amount_in_atm
    global s1,s2,s3,s4
    os.system('cls')
    amount=int(input("Enter the amount to be added: "))
    Amount_in_atm = Amount_in_atm + amount
    print(" ")

    q1=int(input("Enter the number of 2000 notes: "))
    q2=int(input("Enter the number of 500 notes: "))
    q3=int(input("Enter the number of 200 notes: "))
    q4=int(input("Enter the number of 100 notes: "))
    r=q1*2000+q2*500+q3*200+q4*100
    s1=s1+q1
    s2=s2+q2
    s3=s3+q3
    s4=s4+q4
    if(r==amount):
        os.system('cls')
        print("Amount updated successfully")
        sk1="Amount updated by admin "+b['adminname']+" is "+str(amount)
        adminlist.append(sk1)
        print(" ")
        print(" ")
        print("Total no. of 2000's notes after updation:",s1)
        print("Total no. of 500's notes after updation:",s2)
        print("Total no. of 200's notes after updation:",s3)
        print("Total no. of 100's notes after updation:",s4)
        print(" ")
        log=input("To logout please type 1 :")
        if(log=="1"):
            os.system('cls')
            return adminhome(b)
        else:
            print("Please type 1")
    else:
        print("Kindly check the amount")
        print(" ")
        return adminhome(b)

def atmstock(b):
    os.system('cls')
    global Amount_in_atm
    print("Total amount in ATM:", Amount_in_atm )
    print(" ")
    print("Number of 2000's notes:",s1)
    print("Number of 500's notes:",s2)
    print("Number of 200's notes:",s3)
    print("Number of 100's notes:",s4)
    print(" ")
    logg=input("To logout please type 1 :")
    if(logg=="1"):
        print("Thank you for using ATM")
        os.system('cls')
        return adminhome(b)
    else:
        print("Please type 1")

def pinchange(a):
    otp_given=3452
    os.system('cls')
    otp=int(input("Enter the otp sent to your mobile number 67xxxxxx98 : "))
    print(" ")
    if(otp_given==otp):
        new_pin=input("Enter new pin:")
        a['password']=new_pin
        print(" ")
        print("Pin number updated successfully")
        print(" ")
        logo=input("To log out press 1:")
        if(logo=="1"):
            os.system('cls')
            return customerhome(a)
    else:
        print("Invalid otp")
        os.system('cls')
        return customerhome(a)
    
def adminid():
    os.system('cls')
    print("Welcome to Admin portal")
    print(" ")
    adminname=str(input("Enter admin name: "))
    password=input("Enter password: ")
    z={'adminname':adminname,'password':password}
    checkusername(z)

def balance(a):
    os.system('cls')
    Total_amount=a['balance']
    print("Your balance amount is ",Total_amount)
    print(" ")
    print("Thank you")
    logw=int(input("To logout please type 1 :"))
    while(logw==1):
        os.system('cls')
        return customerhome(a)

def withdrawn(a):
    global Amount_in_atm
    os.system('cls')
    Total_amount=a['balance']    
    withdrawn_money=int(input("Enter the amount to be withdrawn : "))
    if(withdrawn_money>Amount_in_atm):
        print(" ")
        print("Not enough cash in ATM")
        print(" ")
        log=int(input("To log out please type 1:"))
        if(log==1):
            return customerhome(a)
    elif(withdrawn_money>Total_amount):
        print(" ")
        print("Not enough cash in your account")
        print(" ")
        log=int(input("To log out please type 1:"))
        if(log==1):
            return customerhome(a)
    else:
        print(" ")
        print("Please wait....")
        print(" ")
        if(a['bank']=='sbi'):
            a['tcount']=a['tcount']+1
            if(a['tcount']==4):
                print("Your have reached your daily withdrawal limit...")
                print("Please visit bank for further details")
            else:
                a['withdrawan amount']=a['withdrawan amount']+withdrawn_money
                if(a['withdrawan amount']>50000):
                    print("You cannot withdraw amount more than Rs. 50000/- per day")
                    print("If you want to withdraw amount Rs.200/- will be deducted from your account")
                    print(" ")
                    kk=int(input("Type 1 for continue transaction else type 2 to return home screen : "))
                    if(kk==1):
                        withdrawn_money=withdrawn_money-200
                        Amount_in_atm=Amount_in_atm-withdrawn_money
                        Balance_money=Total_amount-withdrawn_money
                        sk2=str(Total_amount)
                        sk21=str(withdrawn_money)
                        sk22=str(Balance_money)
                        k={'user':a['name'],'password':a['password'],'totalamount':sk2,'withdrawn':sk21,'balance':sk22}
                        transaction_history_list.append(k)
                        notes=[2000,500,200,100]
                        cashcounter=[0,0,0,0]
                        l=[]
                        for i,j in zip(notes,cashcounter):
                            if(withdrawn_money>=i):
                                j=withdrawn_money//i
                                withdrawn_money= withdrawn_money - j*i
                                l.append(i)
                                l.append(j)
                                updatestock(l)
                        print(" ")
                        print(*l)
                        print(" ")
                        print("Please collect your cash")
                        print(" ")

                        print("Balance amount in your account:",Balance_money)
                        a['balance']=Balance_money
                    else:
                        return customerhome(a)
                else:
                    Amount_in_atm=Amount_in_atm-withdrawn_money
                    Balance_money=Total_amount-withdrawn_money
                    sk2=str(Total_amount)
                    sk21=str(withdrawn_money)
                    sk22=str(Balance_money)
                    k={'user':a['name'],'password':a['password'],'totalamount':sk2,'withdrawn':sk21,'balance':sk22}
                    transaction_history_list.append(k)
                    notes=[2000,500,200,100]
                    cashcounter=[0,0,0,0]
                    l=[]
                    for i,j in zip(notes,cashcounter):
                        if(withdrawn_money>=i):
                            j=withdrawn_money//i
                            withdrawn_money= withdrawn_money - j*i
                            l.append(i)
                            l.append(j)
                            updatestock(l)
                    print(*l)
                    print(" ")
                    print("Please collect your cash")
                    print(" ")

                    print("Balance amount in your account:",Balance_money)
                    a['balance']=Balance_money
        else:
            a['tcount']=a['tcount']+1
            if(a['tcount']==4):
                print("Your have reached your daily withdrawal limit...")
                print("Please visit bank for further details")
            else:
                a['withdrawan amount']=a['withdrawan amount']+withdrawn_money
                if(a['withdrawan amount']>50000):
                    print("You cannot withdraw amount more than Rs. 50000/- per day")
                    print("If you want to withdraw amount Rs.500/- will be deducted from your account")
                    kk=int(input("Type 1 for continue transaction else type 2 to return home screen : "))
                    if(kk==1):
                        withdrawn_money=withdrawn_money-500
                        Amount_in_atm=Amount_in_atm-withdrawn_money
                        Balance_money=Total_amount-withdrawn_money
                        sk2=str(Total_amount)
                        sk21=str(withdrawn_money)
                        sk22=str(Balance_money)
                        k={'user':a['name'],'password':a['password'],'totalamount':sk2,'withdrawn':sk21,'balance':sk22}
                        transaction_history_list.append(k)
                        notes=[2000,500,200,100]
                        cashcounter=[0,0,0,0]
                        l=[]
                        for i,j in zip(notes,cashcounter):
                            if(withdrawn_money>=i):
                                j=withdrawn_money//i
                                withdrawn_money= withdrawn_money - j*i
                                l.append(i)
                                l.append(j)
                                updatestock(l)
                        print(*l)
                        print("Please collect your cash")
                        print(" ")

                        print("Balance amount in your account:",Balance_money)
                        a['balance']=Balance_money
                    else:
                        return customerhome(a)

                else:
                    print("Rs.100/- will be deducted for the amount transfer from",a['bank'],"bank.")
                    withdrawn_money=withdrawn_money-100
                    Amount_in_atm=Amount_in_atm-withdrawn_money
                    Balance_money=Total_amount-withdrawn_money
                    sk2=str(Total_amount)
                    sk21=str(withdrawn_money)
                    sk22=str(Balance_money)
                    k={'user':a['name'],'password':a['password'],'totalamount':sk2,'withdrawn':sk21,'balance':sk22}
                    transaction_history_list.append(k)
                    notes=[2000,500,200,100]
                    cashcounter=[0,0,0,0]
                    l=[]
                    for i,j in zip(notes,cashcounter):
                        if(withdrawn_money>=i):
                            j=withdrawn_money//i
                            withdrawn_money= withdrawn_money - j*i
                            l.append(i)
                            l.append(j)
                            updatestock(l)
                    print(*l)
                    print("Please collect your cash")
                    print(" ")

                    print("Balance amount in your account:",Balance_money)
                    a['balance']=Balance_money

        print(" ")
        log=int(input("To log out please type 1:"))
        if(log==1):
            return customerhome(a)

def updatestock(l):
    global s1,s2,s3,s4
    for i in range(0,len(l)-1):
        if(l[i]==2000):
            k=l[i+1]
            s1=s1-k
        elif(l[i]==500):
            k=l[i+1]
            s2=s2-k
        elif(l[i]==200):
            k=l[i+1]
            s3=s3-k
        elif(l[i]==100):
            k=l[i+1]
            s4=s4-k

def customerhome(a):
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. Money Withdrawal")
    print("2. Balance enquiry")
    print("3. Pin change")
    print("4. Transaction History")
    print("5. Deposit money")
    print("6. Exit")
    print(".........")
    p=int(input("Enter your Choice: "))
    if(p==2):
        balance(a)
    elif(p==1):
        withdrawn(a)
    elif(p==3):
        pinchange(a)
    elif(p==4):
        transaction_history(a)
    elif(p==5):
        deposit(a)
    elif(p==6):
        exitid()
    else:
        print("Invalid")
        return customerhome(a)

def deposit(a):
    os.system('cls')
    global s1,s2,s3,s4
    w=int(input("Enter the amount to be deposited in your account : "))
    a['balance']=a['balance']+w
    q1=int(input("Enter the number of 2000 notes: "))
    q2=int(input("Enter the number of 500 notes: "))
    q3=int(input("Enter the number of 200 notes: "))
    q4=int(input("Enter the number of 100 notes: "))
    s1=s1+q1
    s2=s2+q2
    s3=s3+q3
    s4=s4+q4
    print("Money added to your account")
    log=int(input("To log out please type 1:"))
    if(log==1):
        return customerhome(a)

def transaction_history(a):
    os.system('cls')
    print("Transactions done by the user",a['name'])
    print(" ")
    for i in transaction_history_list:
        if((i['user']==a['name']) and (i['password']==a['password'])):
            print("Total amount in account   : ",i['totalamount'])
            print("Money withdrawn           : ",i['withdrawn'])
            print("Balance amount            : ",i['balance'])
            print("_____________________________________________")
            print(" ")
    log=int(input("To log out please type 1:"))
    if(log==1):
        return customerhome(a)

def checkcustomer(p):
    global c
    for i in l1:
        if((i['name']==p['username']) and (i['password']==p['userpassword'])):
            print("Welcome",p['username'])
            a=i
            return customerhome(a)
    else:
        print("Invalid input")
        c+=1
        if(c==3):
            os.system('cls')
            print("Too many attempts...")
            print(" ")
            print("Please try later...")
        else:
            return home()

def customerid():
    os.system('cls')
    print("Welcome to our ATM")
    print(" ")
    customername=str(input("Enter user name: "))
    customerpassword=input("Enter Password: ")
    p={'username':customername,'userpassword':customerpassword}
    checkcustomer(p)

def exitid():
    os.system('cls')
    return home()

def exitportal():
    os.system('cls')
    print(" ")
    print("Thank you for using our ATM")
    print(" ")
    quit()

def home():
    os.system('cls')
    print("Welcome")
    print("1. Admin login")
    print("2. Customer login")
    print("3. Exit")
    print(".........")
    n=int(input("Enter your Choice: "))
    if(n==1):
        adminid()
    elif(n==2):
        customerid()
    elif(n==3):
        exitportal()
    else:
        print("invalid")
home()
