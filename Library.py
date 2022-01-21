import os
from operator import itemgetter
import datetime
from datetime import date
import time
admin_list=[{'name':'g','password':1}]
books=[{'bookname':'Sports','isbn':123,'quantity':11,'cost':1200},{'bookname':'Who','isbn':121,'quantity':10,'cost':750},{'bookname':'ab','isbn':17,'quantity':20,'cost':200},{'bookname':'vk','isbn':18,'quantity':30,'cost':300}]
users=[]
book_borrow=[]
view_my_books=[]
cart_list=[]
return_approval=[]
current_date="10/12/20"
idd=100

def userid():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. Existing user. Log in to your account")
    print("2. New user. Create a new account")
    print("3. Return to home screen")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        userlogin()
    elif(n==2):
        usercreate()
    else:
        exittohome()

def userlogin():
    os.system('cls')
    print("Log in to your user account")
    print(" ")
    useridd=int(input("Enter your user id : "))
    password=int(input("Enter user password : "))
    p={'id':userid,'password':password}
    for i in users:
        if((i['id']==useridd) and (i['password']==password)):
            b=i
            return userhome(b)
    print(" ")
    print("Username not found")
    print(" ")
    log=int(input("Type 1 to return home screen : "))
    if(log==1):
        return userid()

def usercreate():
    os.system('cls')
    print("Create a new account")
    print(" ")
    username=input("Enter new user name : ")
    userpassword= int(input("Enter new user password : "))
    z=useridgenerate()
    print(" ")
    print("By creating an user account, you need to pay Rs.1500/- as Caution deposit.")
    print("The amount will be refunded on closure of account")
    print(" ")
    print("------------------")
    print("Your userid id",z)
    print("------------------")
    p={'name':username,'id':z,'password':userpassword,'wallet':1500,'bookcount':0}
    users.append(p)
    print(" ")
    print("User account created sucessfully...")
    print(" ")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return userid()

def userhome(b):
    os.system('cls')
    print("Welcome",b['name'])
    print(" ")
    print("1. My profile")
    print("2. View all Books")
    print("3. Search a Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Update book is lost")
    print("7. Return to home screen")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        my_profile(b)
    elif(n==2):
        all_books(b)
    elif(n==3):
        book_search(b)
    elif(n==4):
        borrow_book(b)
    elif(n==5):
        return_book(b)
    elif(n==6):
        book_lost(b)
    else:
        exittohome()

def my_profile(b):
    os.system('cls')
    print("Welcome",b['name'])
    print(" ")
    print("-------------------------")
    print("User name  : ",b['name'])
    print("User Id    : ",b['id'])
    print("-------------------------")
    print(" ")
    print("1. View Borrowed book History")
    print("2. View cart")
    print("3. Check Wallet balance")
    print("4. Add amount to wallet")
    print("5. Exit")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        borrowed_book_history(b)
    elif(n==2):
        view_my_cart(b)
    elif(n==3):
        os.system('cls')
        print("Wallet")
        print(" ")
        print("Available balance is ",b['wallet'])
        print(" ")
        log=int(input("Type 1 to return home screen : "))
        if(log==1):
            return my_profile(b)
    elif(n==4):
        os.system('cls')
        print("Add amount to your wallet")
        print(" ")
        s=int(input("Enter the amount to be added : "))
        print(" ")
        b['wallet']=b['wallet']+s
        print("Amount added successfully")
        print(" ")
        log=int(input("Type 1 to return home screen : "))
        if(log==1):
            return my_profile(b)
    else:
        return userhome(b)

def book_lost(b):
    os.system('cls')
    print("Update here if the borrowed book is lost")
    print(" ")
    k=int(input("Enter the ISBN number of a book : "))
    for i in book_borrow:
        if((i['userid']==b['id']) and (i['isbn']==k)):
            print("Book name    : ",i['bookname'])
            print("ISBN number  : ",i['isbn'])
            print("Book cost    : ",i['cost'])
            k1=i['userid']
    print("____________________________________________")
    print(" ")
    print("Please confirm the details of a book you borrowed.")
    print("If a book is lost, 50% of book cost is collected as fine...")
    print(" ")
    x=int(i['cost'])
    y=x//2
    print("-------------------------------")
    print("Amount to be paid : Rs.",y,"/-")
    print("-------------------------------")
    print(" ")
    m=int(input("Enter 1 to pay : "))
    if(m==1):
        print(" ")
        b['wallet']=b['wallet']-y
        print("Amount paid successfully...")
        for i in view_my_books:
            if((i['userid']==k1) and (i['isbn']==k)):
                i['status']="Book Lost [Amount paid]"
        for i in book_borrow:
            if((i['userid']==k1) and (i['isbn']==k)):
                book_borrow.remove(i)
        log=int(input("Type 1 to return home screen : "))
        if(log==1):
            return userhome(b)
    else:
        return userhome(b)

def view_my_cart(b):
    os.system('cls')
    print("My Cart")
    print(" ")
    print("Userid      : ",b['id'])
    for i in cart_list:
        if(i['id']==b['id']):
            print("-----------------------------")
            print(" ")
            print("Book name   : ",i['bookname'])
            print("ISBN number : ",i['isbn'])
    print("_____________________________________")
    print(" ")
    log=int(input("Type 1 to return home screen : "))
    if(log==1):
        return my_profile(b)

def all_books(b):
    os.system('cls')
    os.system('cls')
    print("Details of all books available in the library")
    print(" ")
    s=sorted(books,key=itemgetter('bookname'))
    for i in s:
        print("Book name    : ",i['bookname'])
        print("ISBN number  : ",i['isbn'])
        print("Stock        : ",i['quantity'])
        print("----------------------------------")
        print(" ")
    print(" ")
    log=int(input("Type 1 to return home screen : "))
    if(log==1):
        return userhome(b)

def book_search(b):
    os.system('cls')
    print("Search a book by name or ISBN number")
    print(" ")
    print("1. Search a book by name")
    print("2. Search a book by ISBN number")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        os.system('cls')
        bookname=input("Enter book name to search : ")
        print(" ")
        for i in books:
            if(i['bookname']==bookname):
                print("Book name    : ",i['bookname'])
                print("ISBN number  : ",i['isbn'])
                print("Stock        : ",i['quantity'])
                print("----------------------------------")
                print(" ")
                print("[1] Add a book to a cart // [2] Return to user screen")
                log=int(input("Enter your choice : "))
                if(log==1):
                    print(" ")
                    isbn=int(input("Enter the isbn number of a book : "))
                    for i in books:
                        if(i['isbn']==isbn):
                            v={'id':b['id'],'bookname':i['bookname'],'isbn':isbn}
                            cart_list.append(v)
                            print(" ")
                            print("Book added to cart")
                            print(" ")
                else:
                    return userhome(b)
    else:
        os.system('cls')
        booknumber=int(input("Enter ISBN number of a book : "))
        print(" ")
        for i in books:
            if(i['isbn']==booknumber):
                print("Book name    : ",i['bookname'])
                print("ISBN number  : ",i['isbn'])
                print("Stock        : ",i['quantity'])
                print("----------------------------------")
                print(" ")
                print("[1] Add a book to a cart // [2] Return to user screen")
                print(" ")
                log=int(input("Enter your choice : "))
                if(log==1):
                    print(" ")
                    isbn=int(input("Enter the isbn number of a book : "))
                    for i in books:
                        if(i['isbn']==isbn):
                            v={'id':b['id'],'bookname':i['bookname'],'isbn':isbn}
                            cart_list.append(v)
                            print(" ")
                            print("Book added to cart")
                            print(" ")
            else:
                return userhome(b)
    print(" ")
    f=int(input("Enter 1 to return user screen : "))
    if(f==1):
        os.system('cls')
        return userhome(b)
    
def borrow_book(b):
    os.system('cls')
    print("The book that borrowed from library must be returned within 15 days. If not fine will be deducted every following day.")
    print(" ")
    w=input("Enter book name : ")
    print(" ")
    s1=b['wallet']
    for i in books:
        if(i['bookname']==w):
            print("Book name    : ",i['bookname'])
            print("ISBN number  : ",i['isbn'])
            print("Stock        : ",i['quantity'])
            print("----------------------------------")
            print(" ")
    e=int(input("Enter ISBN number of a book : "))
    print(" ")
    for j in users:
        if(j['id']==b['id']):
            r=j['bookcount']
        else:
            r=0
    for i in book_borrow:
        if(i['userid']==b['id']):
            if(i['isbn']==e):
                print(" ")
                print("You cannot take a book twice...")
                print(" ")
                break
    else:
        for i in books:
            if(i['isbn']==e):
                if(i['quantity']>0):
                    if(r<3):
                        if(s1>500):
                            rr=due_date()
                            k=rr
                            s=str(k)
                            ee=s[:10]
                            q={'userid':b['id'],'bookname':i['bookname'],'isbn':e,'duedate':ee,'cost':i['cost']}
                            q1={'userid':b['id'],'bookname':i['bookname'],'isbn':e,'status':'Not Returned','duedate':ee}
                            view_my_books.append(q1)
                            book_borrow.append(q)
                            i['quantity']=i['quantity']-1
                            for i in users:
                                if(i['id']==b['id']):
                                    i['bookcount']=i['bookcount']+1
                            print("Book borrowed succussfully...")
                            print(" ")
                            print("Book must be returned within 15 days. ENJOY READING!!!")
                            print("------------------------------------")
                            print("Due date to return the book is",ee)
                            print("------------------------------------")
                            for i in cart_list:
                                if((i['id']==b['id']) and (i['isbn']==e)):
                                    cart_list.remove(i)
                        else:
                            print("Your wallet balance is less than Rs.500/-")
                            print("You can't borrow a book... Update your wallet money to borrow books...")
                    else:
                        print("You have already borrowed 3 books from the library.")
                        print("You can have only 3 books at a time. Kindly return the book before taking another book")
                else:
                    print("No stock available")
    print(" ")
    log=int(input("Type 1 to return user screen : "))
    if(log==1):
        return userhome(b)

def due_date():
    global current_date
    current_date_temp = datetime.datetime.strptime(current_date, "%m/%d/%y")
    new_date = current_date_temp + datetime.timedelta(days=15)
    return new_date

def return_book(b):
    os.system('cls')
    print("Return a book")
    print(" ")
    bookisbn=int(input("Enter the ISBN number of a book : "))
    for i in book_borrow:
        if(b['id']==i['userid']):
            if(i['isbn']==bookisbn):
                return_approval.append(i)
                print(" ")
                print("Please wait for the admin approval.")
                print("Once admin approved, the book will be returned")
    print(" ")
    print("---------------------------------------------------")
    log=int(input("Type 1 to return user screen : "))
    if(log==1):
        return userhome(b)

def borrowed_book_history(b):
    os.system('cls')
    print("History of books taken from the library")
    print(" ")
    z=b['id']
    print("-------------------------")
    print("Username  : ",b['name'])
    print("Userid    : ",z)
    print("-------------------------")
    print(" ")
    for i in view_my_books:
        if(i['userid']==z):
            print("Book name   : ",i['bookname'])
            print("ISBN number : ",i['isbn'])
            print("Status      : ",i['status'])
            print(" ")
    print("__________________________________________")
    print(" ")
    log=int(input("Type 1 to return userhome screen : "))
    if(log==1):
        return my_profile(b)

def adminid():
    os.system('cls')
    print("Log in to admin account")
    print(" ")
    adminname=input("Enter admin name : ")
    adminpass=int(input("Enter admin password : "))
    p={'name':adminname,'password':adminpass}
    for i in admin_list:
        if((i['name']==p['name']) and (i['password']==p['password'])):
            a=i
            return adminhome(a)
    else:
        print("Admin id not found. Please check id and password.")
        print(" ")
        log=int(input("Type 1 to return homescreen : "))
        if(log==1):
            return home()

def adminhome(a):
    os.system('cls')
    print("Welcome",a['name'])
    print(" ")
    print("1. Book Details")
    print("2. View all users")
    print("3. Borrowers details")
    print("4. Add new admin")
    print("5. Approval for book return")
    print("6. Log out")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        adminhome2(a)
    elif(n==2):
        view_all_users(a)
    elif(n==3):
        borrow_details(a)
    elif(n==4):
        new_admin(a)
    elif(n==5):
        approval(a)
    else:
        exittohome()

def adminhome2(a):
    os.system('cls')
    print("Welcome",a['name'])
    print(" ")
    print("1. View all Books")
    print("2. Search a Book")
    print("3. Add new Book")
    print("4. Update details of a Book")
    print("5. Update datetime")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        view_all_books(a)
    elif(n==2):
        search_book(a)
    elif(n==3):
        add_new_book(a)
    elif(n==4):
        update_book(a)
    elif(n==5):
        update_time(a)
    else:
        return adminhome(a)

def update_time(a):
    os.system('cls')
    global current_date
    y=input("Enter date : ")
    current_date=y
    print(" ")
    print("Date updated")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def approval(a):
    global current_date
    os.system('cls')
    print("Book returned by user")
    print(" ")
    for i in range(len(return_approval)):
        for i in return_approval:
            print("Userid           : ",i['userid'])
            print("Book ISBN number : ",i['isbn'])
            print("Book name        : ",i['bookname'])
            print("Due date         : ",i['duedate'])
            print("_________________________________________")
            print(" ")
            k=i['userid']
            k2=i['isbn']
            ss=int(input("Enter 1 to continue : "))
            z=str(i['duedate'])
            print(" ")
            formatted_date1 = time.strptime(current_date, "%m/%d/%y")
            formatted_date2 = time.strptime(z, "%Y-%m-%d")
            aa=(formatted_date1 < formatted_date2)
            if(aa==True):
                print("Book is returned within due date...")
                print(" ")
                return_approval.remove(i)
                book_borrow.remove(i)
                for i in view_my_books:
                    if((i['userid']==k) and (i['isbn']==k2)):
                        i['status']="Returned"
                for i in users:
                    if(i['id']==k):
                        i['bookcount']=i['bookcount']-1
                
            else:
                return_approval.remove(i)
                book_borrow.remove(i)
                from datetime import datetime
                st = datetime.strptime(z, "%Y-%m-%d")
                ed = datetime.strptime(current_date, "%m/%d/%y")
                diff = ed.date() - st.date()
                d=(diff.days)
                print("The book is not returned in due time...")
                print("The book is returned after",d,"days from its due date")
                print(" ")
                w=int(d*2)
                print("The fine amount for the book is Rs.",w,"/-")
                print(" ")
                q=int(input("Enter 1 to continue : "))
                for i in users:
                    if(i['id']==k):
                        i['wallet']=i['wallet']-w
                print(" ")
                for i in view_my_books:
                    if((i['userid']==k) and (i['isbn']==k2)):
                        i['status']="Returned"
                for i in users:
                    if(i['id']==k):
                        i['bookcount']=i['bookcount']-1
                print("Fine amount collected successfully...")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def view_all_books(a):
    os.system('cls')
    print("Details of all books available in the library")
    print(" ")
    print("1. View all books sorted by name")
    print("2. View all books sorted by available quantity")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        os.system('cls')
        print("Books sorted by name")
        print(" ")
        s=sorted(books,key=itemgetter('bookname'))
        for i in s:
            print("Book name    : ",i['bookname'])
            print("ISBN number  : ",i['isbn'])
            print("Stock        : ",i['quantity'])
            print("----------------------------------")
            print(" ")
    else:
        os.system('cls')
        print("Books sorted by availability")
        print(" ")
        s=sorted(books,key=itemgetter('quantity'))
        for i in s:
            print("Book name    : ",i['bookname'])
            print("ISBN number  : ",i['isbn'])
            print("Stock        : ",i['quantity'])
            print("----------------------------------")
            print(" ")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def search_book(a):
    os.system('cls')
    print("Search a book by name or ISBN number")
    print(" ")
    print("1. Search a book by name")
    print("2. Search a book by ISBN number")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        os.system('cls')
        bookname=input("Enter book name to search : ")
        print(" ")
        for i in books:
            if(i['bookname']==bookname):
                print("Book name    : ",i['bookname'])
                print("ISBN number  : ",i['isbn'])
                print("Stock        : ",i['quantity'])
                print("----------------------------------")
                print(" ")
    else:
        os.system('cls')
        booknumber=int(input("Enter ISBN number of a book : "))
        print(" ")
        for i in books:
            if(i['isbn']==booknumber):
                print("Book name    : ",i['bookname'])
                print("ISBN number  : ",i['isbn'])
                print("Stock        : ",i['quantity'])
                print("----------------------------------")
                print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def add_new_book(a):
    os.system('cls')
    print("Add new book")
    print(" ")
    bookname=input("Enter book name : ")
    bookisbn=int(input("Enter ISBN number : "))
    stock=int(input("Enter book quantity : "))
    cost=int(input("Enter the cost of a book : "))
    p={'bookname':bookname,'isbn':bookisbn,'quantity':stock,'cost':cost}
    books.append(p)
    print(" ")
    print("Book added successfully...")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def update_book(a):
    os.system('cls')
    print("Update book details")
    print(" ")
    isbn=int(input("Enter ISBN number of a book to update : "))
    print(" ")
    for i in books:
        if(i['isbn']==isbn):
            print("Book name    : ",i['bookname'])
            print("ISBN number  : ",i['isbn'])
            print("Stock        : ",i['quantity'])
            print("----------------------------------")
            print(" ")
            bookstock=int(input("Enter the quantity of a book to be updated : "))
            i['quantity']=i['quantity']+bookstock
            print(" ")
            print("Book quantity updated successfully...")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def view_all_users(a):
    os.system('cls')
    print("Details of users in the library")
    print(" ")
    for i in users:
        print("User name      : ",i['name'])
        print("User id        : ",i['id'])
        print("----------------------------- ")
        print(" ")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def new_admin(a):
    os.system('cls')
    print("Add new admin")
    print(" ")
    adminname=input("Enter new admin name : ")
    adminpass=int(input("Enter new password : "))
    p={'name':adminname,'password':adminpass}
    admin_list.append(p)
    print(" ")
    print("Admin added successfully...")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)
     
def borrow_details(a):
    os.system('cls')
    print("List of users borrowed books from a library...")
    print(" ")
    for i in book_borrow:
        print("---------------------------------")
        print("Userid      : ",i['userid'])
        print("Book name   : ",i['bookname'])
        print("ISBN number : ",i['isbn'])
        print("Due date    : ",i['duedate'])
    print("__________________________________________")
    print(" ")
    log=int(input("Type 1 to return admin screen : "))
    if(log==1):
        return adminhome(a)

def exittohome():
    os.system('cls')
    return home()

def exitt():
    os.system('cls')
    print("Thank you")
    print(" ")
    quit()

def useridgenerate():
    global idd
    idd=idd+1
    return idd

def home():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        adminid()
    elif(n==2):
        userid()
    else:
        exitt()
home()