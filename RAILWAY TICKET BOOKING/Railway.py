import os
user_list=[]
view_train_list=[]
w=[]
z=1000
booking_list=[]
admin_list=[{'name':'Gokul','password':1234}]
station_view_list=[]

def admin():
    os.system('cls')
    print("Welcome")
    print(" ")
    adminname=input("Enter admin name : ")
    adminpass=int(input("Enter admin password : "))
    for i in admin_list:
        if((i['name']==adminname) and (i['password']==adminpass)):
            b=i
            return adminhome(b)
    else:
        print("Invalid")
        log=int(input("Type 1 to log out : "))
        if(log==1):
            return home()

def adminhome(b):
    os.system('cls')
    print("Welcome",b['name'])
    print(" ")
    print("1. View Trains")
    print("2. Add Trains")
    print("3. View all users")
    print("4. Update train details")
    print("5. Exit")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        view_trains(b)
    elif(n==2):
        add_trains(b)
    elif(n==3):
        view_users(b)
    elif(n==4):
        update_train(b)
    elif(n==5):
        exittohome()

def view_users(b):
    os.system('cls')
    print("Passengers list")
    print(" ")
    for i in view_train_list:
        k=i['trainnumber']
        print(" ")
        print("Train number : ",i['trainnumber'])
        print(" ")
        for i in booking_list:
            if(i['trainnumber']==k):
                print("Passenger name  : ",i['name'])
                print("Boarding point  : ",i['start'])
                print("Destination     : ",i['end'])
                print("Booking number  : ",i['bookingno'])
                print("Seat allocated  : ",i['seat'])
                print(" ")
        print("_________________________________________________")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return adminhome(b)

def add_trains(b):
    os.system('cls')
    print("Add new train")
    print(" ")
    trainnumber=int(input("Enter train number : "))
    start=input("Enter Starting station : ")
    end=input("Enter stopping station : ")
    stop=list(input("Enter all stations : ").split())
    seat=int(input("Enter total number of seats : "))
    stops=int(input("Enter total number of stations : "))
    availability=[[0 for j in range(stops)] for i in range(seat)]
    r={'trainnumber':trainnumber,'start':start,'stop':stop,'end':end,'seats':seat,'stops':stops,'availability':availability}
    view_train_list.append(r)
    c={'train':trainnumber,'stops':stop}
    station_view_list.append(c)
    print(" ")
    print("Train updated successfully")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return adminhome(b)

def view_trains(b):
    os.system('cls')
    print("List of all trains")
    print(" ")
    for i in view_train_list:
        print("Train number        : ",i['trainnumber'])
        print("Starting point      : ",i['start'])
        print("Destination         : ",i['end'])
        print(" ")
        print("Stops               : ",i['stop'])
        print("Total seats         : ",i['seats'])
        print("Total stops         : ",i['stops'])
        print("------------------------------------------")
        print(" ")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return adminhome(b)

def update_train(b):
    os.system('cls')
    print("Update train details")
    print(" ")
    trainnumber=int(input("Enter train number to update : "))
    for i in view_train_list:
        if(i['trainnumber']==trainnumber):
            k=int(input("Enter number of seats to be updated : "))
            i['seats']=i['seats']+k
    print(" ")
    print("Seats updated successfully")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return adminhome(b)

def view_all_trains(a):
    os.system('cls')
    print("List of all trains available...")
    print(" ")
    for i in view_train_list:
        print("Train number        : ",i['trainnumber'])
        print("Starting point      : ",i['start'])
        print("Destination         : ",i['end'])
        print(" ")
        print("Stops               : ",i['stop'])
        print("Total seats         : ",i['seats'])
        print("Total stops         : ",i['stops'])
        print("------------------------------------------")
        print(" ")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return userhome(a)

def search_train(a):
    os.system('cls')
    trainstart=input("Enter starting station : ")
    trainend=input("Enter destination : ")
    print(" ")
    for i in view_train_list:
        s=i['stop']
        if trainend in s and trainstart in s:
            p1=s.index(trainstart)
            p2=s.index(trainend)
            if(p1<p2):
                print("Train number        : ",i['trainnumber'])
                print("Starting point      : ",i['start'])
                print("Destination         : ",i['end'])
                print(" ")
                print("Stops               : ",i['stop'])
                print("Total seats         : ",i['seats'])
                print("Total stops         : ",i['stops'])
                print("------------------------------------------")
    print(" ")
    k=int(input("To book a ticket type 1 [or] To return home screen type 2 : "))
    if(k==1):
        book_tickets(a)
    else:
        return userhome(a)

def book_tickets(a):
    os.system('cls')
    train=int(input("Enter train number : "))
    for i in view_train_list:
        if(i['trainnumber']==train):
            print("Please confirm before booking")
            print(" ")
            print("Train number        : ",i['trainnumber'])
            print("Starting point      : ",i['start'])
            print("Destination         : ",i['end'])
            print(" ")
            print("Stops               : ",i['stop'])
            print("Total seats         : ",i['seats'])
            print("Total stations      : ",i['stops'])
            print("------------------------------------------")
            print(" ")
            seats=i['seats']
            station=i['stops']
            l=i['availability']
    print(" ")
    n=int(input("Enter No.of bookings : "))
    print(" ")
    for p in range(n):
        os.system('cls')
        kk=1
        for i in station_view_list:
            if(i['train']==train):
                pp=i['stops']
            for i in pp:
                print("Station",kk,":",i)
                kk+=1
        print(" ")
        st=int(input("Enter boarding point [station number] : "))
        ed=int(input("Enter destination [station number] : "))
        for i in range(seats):
            if(sum(l[i][st-1:ed-1])==0):
                print(" ")
                t=idgenerate()
                print("---------------------------------")
                print("Your booking number is",t)
                print("---------------------------------")
                print(" ")
                print("Ticket booked")
                print(" ")
                print("Boarding station  : ",pp[st-1])
                print("Departure         : ",pp[ed-1])
                print(" ")
                print("Your seat number is",i)
                print(" ")
                print("____________________________________________")
                print(" ")
                r=int(input("Enter 1 to continue : "))
                y={'name':a['name'],'trainnumber':train,'start':pp[st-1],'end':pp[ed-1],'bookingno':t,'seat':i}
                booking_list.append(y)
                for j in range(st-1,ed):
                    l[i][j]=t
                break
        else:
            t=idgenerate()
            x={'name':a['name'],'trainnumber':train,'bookingno':t,'start':st,'end':ed,'start1':pp[st-1],'end1':pp[ed-1]}
            w.append(x)
            print(" ")
            print("Your booking number is",t)
            print(" ")
            print("No seats available right now...")
            print("Your booking is on waiting list. We will notify you when the ticket is booked.")
            print("-----------------------------------------------------------------------------------")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return userhome(a)

def booking_history(a):
    os.system('cls')
    print("Welcome",a['name'])
    print(" ")
    print("Booking history")
    print(" ")
    for i in booking_list:
        if(i['name']==a['name']):
            print("Train number     : ",i['trainnumber'])
            print("Boarding point   : ",i['start'])
            print("Destination      : ",i['end'])
            print("Booking id       : ",i['bookingno'])
            print("Seat number      : ",i['seat'])
            print("_________________________________________")
            print(" ")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return userhome(a)

def idgenerate():
    global z
    z=z+1
    return z

def cancel_booking(a):
    print("Welcome",a['name'])
    os.system('cls')
    e=int(input("Enter train number : "))
    k=int(input("Enter booking number : "))

    for i in view_train_list:
        if(i['trainnumber']==e):
            l=i['availability']
            q1=i['seats']
            q2=i['stops']
    for i in booking_list:
        if((i['name']==a['name']) and (i['bookingno']==k)):
            for i in range(q1):
                for j in range(q2):
                    if(l[i][j]==k):
                        l[i][j]=l[i][j]-k
            for i in l:
                print(*i)
            for i in booking_list:
                if(i['bookingno']==k):
                    booking_list.remove(i)
            waitcheck(a)
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return userhome(a)

def waitcheck(a):
    os.system('cls')
    if(len(w)==0):
        print("Ticket cancelled successfully...")
        print(" ")
        log=int(input("Enter 1 to return home screen : "))
        if(log==1):
            return userhome(a)
    for i in w:
        name=i['name']
        start=i['start']
        end=i['end']
        trains=i['trainnumber']
        t=i['bookingno']
    for i in station_view_list:
        if(i['train']==trains):
            pp=i['stops']
    for i in view_train_list:
        if(i['trainnumber']==trains):
            l=i['availability']
            seats=i['seats']
    for i in range(seats):
        if(sum(l[i][start-1:end-1])==0):
            for j in range(start-1,end):
                l[i][j]=t
            break
    e={'name':name,'seat':i,'start':pp[start-1],'end':pp[end-1],'trainnumber':trains,'bookingno':t}
    booking_list.append(e)
    for i in w:
        if(t==i['bookingno']):
            w.remove(i)
    print("Ticket cancelled successfully...")
    print(" ")

def waiting(a):
    os.system('cls')
    print("Waiting list tickets")
    print(" ")
    for i in w:
        if(a['name']==i['name']):
            print("Train number    : ",i['trainnumber'])
            print("Booking number  : ",i['bookingno'])
            print("Boarding point  : ",i['start1'])
            print("Destination     : ",i['end1'])
            print(" _______________________________________")
    print(" ")
    print("Once the ticket is booked, the details in the waiting list will get removed...")
    print(" ")
    log=int(input("Type 1 to log out : "))
    if(log==1):
        return userhome(a)

def userhome(a):
    os.system('cls')
    print("Welcome",a['name'])
    print(" ")
    print("1. View trains and availability")
    print("2. Search trains")
    print("3. Book tickets")
    print("4. Cancel train tickets")
    print("5. View booking history")
    print("6. Waiting list")
    print("7. Exit to home screen")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        view_all_trains(a)
    elif(n==2):
        search_train(a)
    elif(n==3):
        book_tickets(a)
    elif(n==4):
        cancel_booking(a)
    elif(n==5):
        booking_history(a)
    elif(n==6):
        waiting(a)
    else:
        exittohome()
    
def userlogin():
    os.system('cls')
    print("Log in your user account")
    print(" ")
    username=input("Enter your username : ")
    userpassword=int(input("Enter your user password : "))
    print(" ")
    for i in user_list:
        if((i['name']==username) and i['password']==userpassword):
            a=i
            return userhome(a)
    else:
        print("Invalid username or password")
        log=int(input("Type 1 to log out : "))
        if(log==1):
            return user()

def usercreate():
    os.system('cls')
    print("Create a new account")
    print(" ")
    username=input("Enter your name : ")
    userpassword=int(input("Create a strong password : "))
    u={'name':username,'password':userpassword}
    user_list.append(u)
    print(" ")
    print("Account created successfully")
    print("Kindly login to your user account in the login page.")
    print(" ")
    log=int(input("Type 1 to return login page : "))
    if(log==1):
        return user()

def user():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. New user. Create an account")
    print("2. Already have an account. Log in your account")
    print("3. Exit to home screen")
    print(" ")
    n=int(input("Please enter your choice : "))
    if(n==1):
        usercreate()
    elif(n==2):
        userlogin()
    else:
        exittohome()

def exitportal():
    os.system('cls')
    print("Thank you for using our service")
    print(" ")
    quit()

def exittohome():
    os.system('cls')
    return home()

def home():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1. Admin page")
    print("2. User login")
    print("3. Exit")
    print(" ")
    n=int(input("Please enter your choice : "))
    if(n==1):
        admin()
    elif(n==2):
        user()
    else:
        exitportal()
home()