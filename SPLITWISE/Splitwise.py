from collections import UserList
import os
users=[]
userid=100
grpid=2000
expenseid=0
view_all_expense=[]
need_to_pay=[]
recieve_payment=[]
recieve_payment1=[]
payment_recieve=[]
payment_recieve1=[]
paid_list=[]
paid_list1=[]
history=[]
history1=[]
groups=[]
need_to_pay1=[]

def usercreate():
    os.system('cls')
    print("------Create your user account------")
    print(" ")
    name=input("Enter your name : ")
    password=int(input("Create new password [0-9] : "))
    print(" ")
    wallet=int(input("Enter your wallet amount : "))
    z=idgenerate()
    d={'name':name,'password':password,'id':z,'wallet':wallet}
    users.append(d)
    print(" ")
    print("Your userid is",z)
    print("------------------")
    print(" ")
    print("Account created successfully")
    print(" ")
    log=input("Press Enter to log out...")
    return home()

def userlogin():
    os.system('cls')
    print("------Log in to your user account------")
    print(" ")
    userid=int(input("Enter your userid : "))
    password=int(input("Enter your user password : "))
    print(" ")
    for i in users:
        if((i['id']==userid) and (i['password']==password)):
            a=i
            userhome(a)
    print("User Id not found")
    print(" ")
    print("-------------------------------------------")
    log=input("Press Enter to log out...")
    return home()

def userhome(a):
    os.system('cls')
    print("------Welcome",a['name'],"------")
    print(" ")
    print("1. View all users")
    print("2. Add an expense")
    print("3. Groups")
    print("4. Check Wallet")
    print("5. Payment")
    print("6. Expense History")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        view_all_users(a)
    elif(n==2):
        add_expense(a)
    elif(n==3):
        groupss(a)
    elif(n==4):
        wallet(a)
    elif(n==5):
        payment(a)
    elif(n==6):
        expense_history(a)
    else:
        return home()

def groupss(a):
    os.system('cls')
    print("------Groups------")
    print(" ")
    print("1. View Groups")
    print("2. Create a group")
    print("3. Group Expense")
    print("4. Delete a group")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        view_groups(a)
    elif(n==2):
        create_group(a)
    elif(n==3):
        group_expense(a)
    elif(n==4):
        delete_group(a)
    else:
        return userhome(a)

def delete_group(a):
    os.system('cls')
    print("------Delete a group------")
    print(" ")
    r=int(input("Enter group id to be deleted : "))
    print(" ")
    for i in groups:
        if((i['groupid']==r) and (i['admin']==a['name'])):
            groups.remove(i)
            print("Group deleted successfully")
            print(" ")
            break
    else:
        print("Only Admin can delete a Group")
        print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)
    
def group_expense(a):
    os.system('cls')
    print("------Group Expense------")
    print(" ")
    e1=int(input("Enter Group ID : "))
    print(" ")
    for i in groups:
        if(i['groupid']==e1):
            b=i
            group_home(b,a)

def group_home(b,a):
    os.system('cls')
    print("Groups")
    print(" ")
    k=b['members']
    print("Group name   : ",b['groupname'])
    print("Group ID     : ",b['groupid'])
    print("Group admin  : ",b['admin'])
    print("Group count  : ",b['count'])
    print(" ")
    print("Group Members")
    bb=1
    for jj in k:
        print(bb,".",jj['id']," : ",jj['name'])
        bb+=1
    print("________________________________________________")
    print(" ")
    print("1. Add an Expense")
    print("2. Add members")
    print("3. Remove members")
    print(" ")
    t=int(input("Enter your Choice : "))
    if(t==1):
        add_group_expense(b,a)
    elif(t==2):
        add_members(b,a)
    elif(t==3):
        remove_members(b,a)
    else:
        return userhome(a)

def add_group_expense(b,a):
    os.system('cls')
    print("------Add a group expense------")
    print(" ")
    expense_list=[]
    expense_list1=[]
    z=expenseidgenerate()
    print("Your Expense ID is",z)
    print("--------------------------")
    print(" ")
    name=input("Enter expense name       : ")
    amount=int(input("Enter total amount       : "))
    print(" ")
    print("-----------------------------------------")
    expense_creator=a['name']
    kk=b['members']
    for i in kk:
        expense_list.append(i)
        expense_list1.append(i)
    os.system('cls')
    print(" ")
    r=int(input("Enter the userid of a person who paid the amount : "))
    for i in expense_list1:
        r1=i['id']
        if(r1==r):
            expense_list1.remove(i)
    for i in expense_list:
        r1=i['id']
        if(r1==r):
            p=i['name']
    m=b['count']
    t1=amount/m
    t=round(t1,2)
    print(" ")
    x=0
    print(" ")
    print("Total amount paid in expense : ",amount)
    print("-------------------------------------------")
    print(" ")
    bb=1
    for i in expense_list:
        r2=int(i['id'])
        if(r2!=r):
            print(bb,".",i['name'],"needs to pay Rs.",t,"to",p)
            print(" ")
            bb+=1
            l={'id':i['id'],'creator':expense_creator,'expenseid':z,'expenselist':expense_list,'totalamount':amount,'amounttopay':t,'expensename':name,'payuser':p,'status':"Not Paid"}
            need_to_pay.append(l)
            need_to_pay1.append(l)
    l1={'id':r,'expenseid':z,'creator':expense_creator,'expenselist':expense_list,'totalamount':amount,'expensename':name,'payuser':p,'amounttopay':t}
    recieve_payment.append(l1)
    recieve_payment1.append(l1)
    w={'expenseid':z,'creator':expense_creator,'expensename':name,'amount':amount,'paidby':p,'payuserid':r,'needtopay':expense_list1,'amounttopay':t}
    history.append(w)
    print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)

def remove_members(b,a):
    os.system('cls')
    print("------Remove a member in a group------")
    print(" ")
    if(a['name']==b['admin']):
        k2=b['members']
        y=int(input("Enter userid of a member : "))
        for j in k2:
            if(j['id']==y):
                k2.remove(j)
                b['count']=b['count']-1
                print(" ")
                print(j['name'],"removed from a group",b['groupname'],"successfully")
        print(" ")
    else:
        print("Only Admin can remove group members")
        print(" ")
    logg=input("Press Enter to log out...")
    return group_home(b,a)

def add_members(b,a):
    os.system('cls')
    print("------Add a member to a group------")
    print(" ")
    if(a['name']==b['admin']):
        k1=b['members']
        y=int(input("Enter userid of a member : "))
        for j in users:
            if(j['id']==y):
                k1.append(j)
                b['count']=b['count']+1
                print(" ")
                print(j['name'],"added to a group",b['groupname'],"successfully")
    else:
        print("Only Admin can add group members")    
    print(" ")
    logg=input("Press Enter to log out...")
    return group_home(b,a)

def view_groups(a):
    os.system('cls')
    print("------List of Groups------")
    print(" ")
    for i in groups:
        k=i['members']
        for j in k:
            if(j['id']==a['id']):
                print("Group name   : ",i['groupname'])
                print("Group ID     : ",i['groupid'])
                print("Group Admin  : ",i['admin'])
                print("Group count  : ",i['count'])
                print(" ")
                print("Group members")
                ba=1
                for jj in k:
                    print(ba,".",jj['id']," : ",jj['name'])
                    ba+=1
                print("-------------------------------------------------")
    print(" ")
    print("__________________________________________________")
    print(" ")
    logg=input("Press Enter to log out...")
    return groupss(a)
        
def create_group(a):
    os.system('cls')
    group_list=[]
    print("------Create Groups------")
    print(" ")
    z=groupid()
    print("Your group ID is",z)
    print("--------------------")
    print(" ")
    group_name=input("Enter Group name : ")
    n=int(input("Enter no. of users : "))
    print(" ")
    admin=a['name']
    for i in range(n):
        userss=int(input("Enter userid : "))
        for f in users:
            if(f['id']==userss):
                group_list.append(f)
    w={'groupname':group_name,'admin':admin,'groupid':z,'members':group_list,'count':n}
    groups.append(w)
    print(" ")
    print("Group created successfully")
    print("__________________________________________________________")
    print(" ")
    logg=input("Press Enter to log out...")
    return groupss(a)


def view_all_users(a):
    os.system('cls')
    print("------List of all users------")
    print(" ")
    for i in users:
        print("User name    : ",i['name'])
        print("User Id      : ",i['id'])
        print("______________________")
        print(" ")
    print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)

def add_expense(a):
    os.system('cls')
    print("------Add an Expense------")
    print(" ")
    expense_list=[]
    expense_list1=[]
    z=expenseidgenerate()
    print("Your Expense id is",z)
    print("----------------------")
    print(" ")
    name=input("Enter expense name       : ")
    amount=int(input("Enter total amount       : "))
    m=int(input("Enter total no. of users : "))
    print(" ")
    print("------------------------------")
    expense_creator=a['name']
    for j in range(m):
        idd=int(input("Enter user id : "))
        print(" ")
        for i in users:
            if(i['id']==idd):
                expense_list.append(i)
                expense_list1.append(i)
    print("-------------------------------")
    print(" ")
    payment_function(z,name,amount,m,expense_list1,expense_list,idd,a,expense_creator)


def payment_function(z,name,amount,m,expense_list1,expense_list,idd,a,expense_creator):
    os.system('cls')
    print(" ")
    r=int(input("Enter the userid of a person who paid the amount : "))
    for i in expense_list1:
        r1=i['id']
        if(r1==r):
            expense_list1.remove(i)
    for i in expense_list:
        r1=i['id']
        if(r1==r):
            p=i['name']
    t1=amount/m
    t=round(t1,2)
    print(" ")
    print("------------------------------")
    print("1. Split Equally")
    print("2. Split Unequally")
    print("------------------------------")
    print(" ")
    k2=int(input("Enter your choice : "))
    if(k2==1):
        os.system('cls')
        x=0
        print(" ")
        print("Total amount paid in expense : ",amount)
        print("-------------------------------------------")
        print(" ")
        bb=1
        for i in expense_list:
            r2=int(i['id'])
            if(r2!=r):
                print(bb,".",i['name'],"needs to pay Rs.",t,"to",p)
                print(" ")
                bb+=1
                l={'id':i['id'],'expenseid':z,'expenselist':expense_list,'totalamount':amount,'amounttopay':t,'expensename':name,'payuser':p,'creator':expense_creator,'status':"Not Paid"}
                need_to_pay.append(l)
                need_to_pay1.append(l)
        l1={'id':r,'expenseid':z,'expenselist':expense_list,'totalamount':amount,'creator':expense_creator,'expensename':name,'payuser':p,'amounttopay':t}
        recieve_payment.append(l1)
        recieve_payment1.append(l1)
        w={'expenseid':z,'expensename':name,'creator':expense_creator,'amount':amount,'paidby':p,'payuserid':r,'needtopay':expense_list1,'amounttopay':t}
        history.append(w)
    else:
        os.system('cls')
        x=0
        print(" ")
        print("Total amount paid in expense : ",amount)
        print("-------------------------------------------")
        print(" ")
        listt=[]
        q=0
        for i in expense_list:
            if(i['id']!=r):
                print("User ID   : ",i['id'])
                print("Username  : ",i['name'])
                print(" ")
                tt=int(input("Enter the amount that the user need to pay : "))
                q=q+tt
                print("---------------------------------------------------------")
                l={'id':i['id'],'creator':expense_creator,'expenseid':z,'expenselist':expense_list,'totalamount':amount,'amounttopay':tt,'expensename':name,'payuser':p,'status':"Not Paid"}
                need_to_pay.append(l)
                need_to_pay1.append(l)
                print(" ")
                w1={'name':i['name'],'creator':expense_creator,'expenseid':z,'id':i['id'],'expensename':name,'amount':amount,'paidby':p,'payuserid':r,'amounttopay':tt}
                history1.append(w1)
        q1=amount-q
        print("Amount to be paid")
        print("---------------------")
        for i in history1:
            xx=str(i['name'])
            print(xx.ljust(8," ")," : ",i['amounttopay'])
        print(" ")
        print("Amount share for",p," : ",q1)
        print("-------------------------------")
        print("Total amount          : ",amount)
        print("---------------------------------")
                
        l1={'id':r,'creator':expense_creator,'payid':i['id'],'expenseid':z,'expenselist':listt,'totalamount':amount,'expensename':name,'payuser':p,'amounttopay':tt}
        recieve_payment.append(l1)
        recieve_payment1.append(l1)
    print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)

def wallet(a):
    os.system('cls')
    print("------Welcome",a['name'],"------")
    print(" ")
    print("Available Balance in the wallet is",a['wallet'])
    print(" ")
    print("___________________________________________________")
    print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)

def payment(a):
    os.system('cls')
    print("------Payment------")
    print(" ")
    for i in recieve_payment:
        if(i['id']==a['id']):
            st=i['expenselist']
            if(len(st)==1):
                recieve_payment.remove(i)
            else:
                print("Expense name      : ",i['expensename'])
                print("Expense Id        : ",i['expenseid'])
                print("Expense Creator   : ",i['creator'])
                print("Total money spent : ",i['totalamount'])
                print(" ")
                h=i['amounttopay']
                bb=1
                o=i['expenseid']
                for i in st:
                    if(i['id']!=a['id']):
                        print(bb,".",i['name'],"needs to pay Rs.",h,"to you")
                        bb+=1
                print(" ")
                print("--------------------------------------------------------")
                cc=1
                for i in paid_list:
                    if(i['eid']==o) and (i['payto']==a['name']):
                        print(cc,".",i['name'],"paid Rs",i['amountpaid'],"----","[Balance =",i['balance'],"]")
                        print(" ")
                        cc+=1
                print("---------------------------------------------------------")

    for i in need_to_pay:
        if(i['id']==a['id']):
            print("______________________________________________________________________")
            print(" ")
            print("Expense name      : ",i['expensename'])
            print("Expense Id        : ",i['expenseid'])
            print("Expense Creator   : ",i['creator'])
            print("Total money spent : ",i['totalamount'])
            print("Amount paid by    : ",i['payuser'])
            print("Balance to pay    : ",i['amounttopay'])
            print(" ")
            print("--------------------------------------------------------")
            print("You need to pay Rs.",i['amounttopay'],"to",i['payuser'])
            print("---------------------------------------------------------")
            print(" ")
            yyy=i['expenseid']
            k=int(input("Enter 1 to pay [or] Enter 2 to continue : "))
            if(k==1):
                print(" ")
                y=float(input("Enter the amount to pay : "))
                print(" ")
                if(y==i['amounttopay']):
                    a['wallet']=a['wallet']-y
                    for u in users:
                        if(u['name']==i['payuser']):
                            u['wallet']=u['wallet']+y
                    for j in need_to_pay:
                        if((j['id']==a['id']) and (j['expenseid']==i['expenseid'])):
                            need_to_pay.remove(j)
                            print("Amount paid successfully...")
                            print("----------------------------------")
                    kk=i['expenselist']
                    i['amounttopay']=0
                    q={'name':a['name'],'eid':i['expenseid'],'payto':i['payuser'],'amountpaid':y,'balance':i['amounttopay'],'status':"Amount Paid"}
                    paid_list.append(q)
                    paid_list1.append(q)
                    for i in kk:
                        if(i['id']==a['id']):
                            kk.remove(i)
                else:
                    for u in users:
                        if(u['name']==i['payuser']):
                            u['wallet']=u['wallet']+y
                    a['wallet']=a['wallet']-y
                    i['amounttopay']=round(i['amounttopay']-y,2)
                    print("Amount paid successfully")
                    print(" ")
                    q={'name':a['name'],'eid':i['expenseid'],'payto':i['payuser'],'amountpaid':y,'balance':i['amounttopay']}
                    paid_list.append(q)
                    print("The balance amount to pay is",i['amounttopay'])
                    print("-------------------------------------------------")
                    print(" ")
                logg1=input("Press Enter to continue...")
                print(" ")
    print("______________________________________________________")
    print(" ")
    log=input("Press Enter to log out...")
    return userhome(a)

def expense_history(a):
    os.system('cls')
    print("------Expense History------")
    print(" ")
    for i in recieve_payment1:
        if(i['id']==a['id']):
            st=i['expenselist']
            print("Expense name      : ",i['expensename'])
            print("Expense Id        : ",i['expenseid'])
            print("Expense Creator   : ",i['creator'])
            print("Total money spent : ",i['totalamount'])
            print("[The payment status is listed below...]")
            print(" ")
            bb=1
            o=i['expenseid']
            t=i['amounttopay']
            print("----------------------------------------------------")
            cc=1
            print("S.no","\t","Name","\t\t","Amountpaid","\t","Balance")
            print("-----------------------------------------------------")
            for i in paid_list:
                if(i['eid']==o) and (i['payto']==a['name']):
                    x=str(cc)
                    yy=str(i['name'])
                    lp=str(i['amountpaid'])
                    tp=str(i['balance'])
                    print(x.ljust(3," "),"\t",yy.ljust(6," "),"\t",lp.ljust(6," "),"\t",tp.ljust(6," "))
                    cc+=1
            print("---------------------------------------------------------")
    print("_________________________________________________________________________________")
    print(" ")

    for u in history:
        kk=u['needtopay']
        for j in kk:
            if(a['id']==j['id']):
                print("Expense name     : ",u['expensename'])
                print("Expense ID       : ",u['expenseid'])
                print("Expense Creator  : ",u['creator'])
                print("Total amount     : ",u['amount'])
                print("Amount paid by   : ",u['paidby'])
                print("Amount to pay    : ",u['amounttopay'])
                print("-------------------------------------------------")
                for j in paid_list1:
                    if((a['name']==j['name']) and (j['eid']==u['expenseid'])):
                        print("Payment status    : ",j['status'])
                print("-------------------------------------------------")
    for d in history1:
        if(a['id']==d['id']):
            print("Expense name     : ",d['expensename'])
            print("Expense ID       : ",d['expenseid'])
            print("Expense Creator  : ",d['creator'])
            print("Total amount     : ",d['amount'])
            print("Amount paid by   : ",d['paidby'])
            print("Amount to pay    : ",d['amounttopay'])
            print("-------------------------------------------------")
            for j in paid_list1:
                if((a['name']==j['name']) and (j['eid']==d['expenseid'])):
                    print("Payment status    : ",j['status'])
            print("-------------------------------------------------")
    print("_________________________________________________________________________________")
    print(" ")
    logg=input("Press Enter to continue...")
    return userhome(a)

def idgenerate():
    global userid
    userid=userid+1
    return userid

def expenseidgenerate():
    global expenseid
    expenseid=expenseid+1
    return expenseid

def groupid():
    global grpid
    grpid=grpid+1
    return grpid

def home():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. New user. Create an account")
    print("2. Log in to your account")
    print("3. Exit")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        usercreate()
    elif(n==2):
        userlogin()
    else:
        os.system('cls')
        print("\nThank you !!!")
        print(" ")
        quit()
home()