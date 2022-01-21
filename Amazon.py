import os
import math
from operator import itemgetter
c=0
c1=0
id=100
admin=[{'name':'gokul','password':'1'}]
merchant=[]
merchant_approve_list=[]
merchant_product_list=[]
merchant_products=[]
merchant_cardlist=[]
product_history=[]
salesreport_list=[]
l2=[]
user=[]
userid=500
productid=1000
productlist=[]
cart_add_list=[]

def adminlogin():
    global admin
    global c
    os.system('cls')
    print("Welcome")
    print(" ")
    admin_name=input("Enter admin name : ")
    admin_password=input("Enter your password : ")
    print(" ")
    for i in admin:
        if((i['name']==admin_name) and (i['password']==admin_password)):
            a=i
            os.system('cls')
            return adminhome()
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

def adminhome():
    print("Welcome")
    print(" ")
    print("1) Add Merchant")
    print("2) Remove Merchant")
    print("3) Approve Merchant")
    print("4) View all Merchants")
    print("5) View all Products")
    print("6) Exit")
    print(" ")
    n1=int(input("Please enter your choice : "))
    if(n1==1):
        addmerchant()
    elif(n1==2):
        removemerchant()
    elif(n1==5):
        view_all_products()
    elif(n1==4):
        view_all_merchant()
    elif(n1==6):
        exitid()
    elif(n1==3):
        approvemerchant()
    else:
        print("Invalid")
        os.system('cls')
        return adminhome()

def view_all_merchant():
    os.system('cls')
    print("List of merchants")
    print(" ")
    for i in merchant:
        print(" ")
        print("Merchant name    : ",i['name'])
        print("Merchantid       : ",i['merchantid'])
        print("_______________________________________")
    print(" ")
    w=int(input("To return homescreen type 1 : "))
    if(w==1):
        os.system('cls')
        return adminhome()

def view_all_products():
    os.system('cls')
    print("Welcome")
    print(" ")
    print("List of products")
    print(" ")
    for i in merchant_product_list:
        print("  Merchant id   : ",i['merchantid'],"          Total price     : ",i['productprice'])
        print("  Product Id    : ",i['productid'],"         Product name    : ",i['product'])
        print("  Discount      : ",i['productdiscount'],"           Discount amount : ",i['Discount Amount'])
        print("  Stock         : ",i['productstock'],"           Product price   : ",i['Discounted product price'])
        print("------------------------------------------------------------------------------------------")
        print(" ")
    print(" ")
    w=int(input("To return homescreen type 1 : "))
    if(w==1):
        os.system('cls')
        return adminhome()

def approvemerchant():
    os.system('cls')
    global merchant_approve_list
    if(len(merchant_approve_list)==0):
        print("No merchants to be approved")
    else:
        for i in merchant_approve_list:
            print(" ")
            print("Merchant id   : ",i['merchantid'])
            print("Merchant name : ",i['name'])
            print(" ")
            admin_approval=input("Approve / Not approve (Yes-Approve No-Not Approve) : ")
            print("______________________________________________________")
            if(admin_approval=='Yes'):
                merchant.append(i)
        merchant_approve_list=[]
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return adminhome()

def addmerchant():
    os.system('cls')
    global merchant
    v=idgenerate()
    print("Merchant id is",v)
    print(" ")
    merchant_username=input("Enter Merchant name : ")
    merchant_userpassword=input("Enter Merchant password : ")
    s={'merchantid':v,'name':merchant_username,'password':merchant_userpassword}
    merchant.append(s)
    print(" ")
    print("Merchant added successfully")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return adminhome()

def removemerchant():
    os.system('cls')
    k=int(input("Enter the merchant id to be removed : "))
    for i in merchant:
        if(k==i['merchantid']):
            merchant.remove(i)
    print(" ")
    print("Merchant removed successfully")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return adminhome()

def exitportal():
    os.system('cls')
    print("Thank you for using Amazon")
    print(" ")
    quit()

def exitid():
    os.system('cls')
    print("Logged out successfully")
    return home()

def idgenerate():
    global id
    id=id+1
    return id

def merchant_id_create():
    os.system('cls')
    print("Welcome")
    print(" ")
    z=idgenerate()
    print("Your user id is",z)
    print(" ")
    merchant_name=input("Enter your name : ")
    merchant_password=input("Create a password : ")
    print(" ")
    x={'merchantid':z,'name':merchant_name,'password':merchant_password}
    merchant_approve_list.append(x)
    print("Id waiting for approval")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchantcheck()

def merchant_id_login():
    os.system('cls')
    global c1
    global merchant
    print("Welcome")
    print(" ")
    merchant_userid=int(input("Enter your userid : "))
    merchant_userpassword=input("Enter userpassword : ")
    z=approvecheck(merchant_userid)
    if(z==True):
        for i in merchant:
            if((merchant_userid==i['merchantid'])and (merchant_userpassword==i['password'])):
                a=i
                return merchanthome(a)
                break
        else:
            print("Invalid input")
            c1+=1
            if(c1==3):
                os.system('cls')
                print("Too many attempts...")
                print(" ")
                print("Please try later...")
            else:
                return home()
    else:
        os.system('cls')
        print("User id is not approved")
        print("Please contact admin")
        print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchantcheck()

def approvecheck(merchant_userid):
    global merchant_approve_list
    for i in merchant_approve_list:
        if(i['merchantid']==merchant_userid):
            return False
    else:
        return True

def merchanthome(a):
    os.system('cls')
    print("Welcome")
    print(" ")
    print("1) Add product")
    print("2) Remove product")
    print("3) Product update")
    print("4) View products")
    print("5) Add card details")
    print("6) Merchant wallet")
    print("7) View Sales report")
    print("8) Exit")
    print(" ")
    n=int(input("Enter your choice : "))
    if(n==1):
        addproduct(a)
    elif(n==2):
        removeproduct(a)
    elif(n==3):
        productstock(a)
    elif(n==4):
        view_product(a)
    elif(n==5):
        card_details(a)
    elif(n==6):
        merchantwallet(a)
    elif(n==7):
        sales_report(a)
    elif(n==8):
        merchantcheck()
    else:
        print("Invalid")
        return merchantcheck()

def sales_report(a):
    os.system('cls')
    print("Sales Report")
    print(" ")
    print("  Userid        Productid        Productname        Quantity        Total amount")
    print("_________________________________________________________________________________")
    for i in salesreport_list:
        if(i['merchantid']==a['merchantid']):
            print(" ") 
            print("  ",i['userid'],"          ",i['productid'],"             ", i['product'],"              ",i['quantity'],"             ",i['amount'])
            print("_________________________________________________________________________________")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchanthome(a)

def card_details(a):
    os.system('cls')
    global merchant_cardlist
    merchant_card=int(input("Enter the card number : "))
    merchant_name=input("Enter card name : ")
    merchant_balance=int(input("Enter available balance : "))
    merchant_productsold=0
    q=a['merchantid']
    d={'merchantid':q,'merchantname':merchant_name,'merchantcard':merchant_card,'balance':merchant_balance,'productssold':merchant_productsold}
    merchant_cardlist.append(d)
    print(" ")
    print("Details updated successfully")
    return merchantwallet(a)

def merchantwallet(a):
    os.system('cls')
    print(" ")
    for i in merchant_cardlist:
        if(a['merchantid']==i['merchantid']):
            merchant_name=i['merchantname']
            merchant_card=i['merchantcard']
            merchant_productsold=i['productssold']
            merchant_balance=i['balance']
            print("Merchant wallet details")
            print(" ")
            print("1) Merchant id                        : ",a['merchantid'])
            print("2) Merchant card name                 : ",merchant_name)
            print("3) Merchant card number               : ",merchant_card)
            print("4) Number of products sold            : ",merchant_productsold)
            print("5) Merchant wallet available balance  : ",merchant_balance)
            print(" ")
    log=int(input("To log out please type 1:"))
    if(log==1):
        os.system('cls')
        return merchanthome(a)

def productstock(a):
    os.system('cls')
    print("Welcome")
    k=input("Enter the product name to update : ")
    for i in merchant_product_list:
        if((i['product']==k) and (i['merchantid']==a['merchantid'])):
            l=int(input("Enter the number of stocks that needs to be updated : "))
            y=int(i['productstock'])
            y=y+l
            i['productstock']=y

            w=int(input("Enter the product price to be updated : "))
            r=int(i['productprice'])
            r=r+w
            i['productprice']=r

            w1=int(input("Enter the product discount to be updated : "))
            h=int(i['productdiscount'])
            h=h+w1
            i['productdiscount']=h

            u=r*h/100
            ul=math.trunc(u)
            i['Discount Amount']=ul

            u1=r-u
            u1l=math.trunc(u1)
            i['Discounted product price']=u1l
            
    print("Product updated")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchanthome(a)
    

def productidgenerate(product):
    global productid
    for i in productlist:
        if(i['product']==product):
            return i['productid']
    else:
        productid=productid+1
        o={'product':product,'productid':productid}
        productlist.append(o)
        return productid

def addproduct(a):
    global merchant_product_list
    os.system('cls')
    print("Welcome")
    print(" ")
    x=a['merchantid']
    product=input("Enter product name : ")
    productprice=int(input("Enter Product price : "))
    productstock=int(input("Enter the product stock : "))
    productdiscount=int(input("Enter product discount : "))
    k=productprice*productdiscount/100
    product_discount_price=math.trunc(k)
    y=productidgenerate(product)
    l=productprice-product_discount_price
    Discounted_product_price=math.trunc(l)
    d={'merchantid':x,'product':product,'productid':y,'productprice':productprice,'productdiscount':productdiscount,'Discount Amount':product_discount_price,'Discounted product price':Discounted_product_price,'productstock':productstock}
    merchant_product_list.append(d)
    print(" ")
    print("Your product id is :",y)
    print(" ")
    print("Product updated successfully")
    print(" ")
    print("1) Add another product")
    print("2) Return to homescreen")
    print(" ")
    r=int(input("Enter your choice: "))
    if(r==1):
        os.system('cls')
        return addproduct(a)
    else:
        return merchanthome(a)

def removeproduct(a):
    os.system('cls')
    u=a['merchantid']
    z=input("Enter the product name to be removed : ")
    for i in merchant_product_list:
        if((i['product']==z) and (i['merchantid']==u)):
            merchant_product_list.remove(i)
            print("Product removed successfully")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchanthome(a)

def view_product(a):
    os.system('cls')
    print("Welcome",a['name'])
    print(" ")
    if(len(merchant_product_list)==0):
        print(" ")
        print("No products here")
    else:
        for i in merchant_product_list:
            if(i['merchantid']==a['merchantid']):
                print("Product details")
                print(" ")
                print("Product name             : ",i['product'])
                print("Product id               : ",i['productid'])
                print("Price                    : ",i['productprice'])
                print("Discount                 : ",i['productdiscount'])
                print("Discount Amount          : ",i['Discount Amount'])
                print("Discounted Product price : ",i['Discounted product price'])
                print("Stock available          : ",i['productstock'])
                print(" ________________________________________________________")
                print(" ")
    print(" ")
    log=int(input("To log out please type 1 : "))
    if(log==1):
        os.system('cls')
        return merchanthome(a)

def merchantcheck():
    os.system('cls')
    print("Welcome to Amazon")
    print(" ")
    print("1) Log in to your Amazon account")
    print("2) New user. Create an Amazon account")
    print("3) Exit")
    print(" ")
    e=int(input("Please enter your choice : "))
    if(e==1):
        merchant_id_login()
    elif(e==2):
        merchant_id_create()
    elif(e==3):
        exitid()
    else:
        print("Invalid")
        return home()

def user_id_login():
    os.system('cls')
    global user
    print("Welcome")
    print(" ")
    user_userid=int(input("Enter your userid : "))
    user_userpassword=int(input("Enter userpassword : "))
    for i in user:
        if((user_userid==i['userid']) and (user_userpassword==i['userpassword'])):
            b=i
            return userhome(b)
    else:
        print("Invalid. Userid not found")
        print(" ")
        k=int(input("Type 1 to return home screen : "))
        if(k==1):
            os.system('cls')
            return usercheck()

def user_id_create():
    os.system('cls')
    print("Welcome to Amazon")
    print(" ")
    w=useridgenerate()
    print("Your user id is",w)
    print(" ")
    user_name=input("Enter your name : ")
    user_password=int(input("Create a password : "))
    card_number1=int(input("Enter the card number : "))
    card_name1=input("Enter card holder name : ")
    card_balance=int(input("Enter balance : "))
    r={'userid':w,'username':user_name,'userpassword':user_password,'cardnumber':card_number1,'cardname':card_name1,'balance':card_balance}
    user.append(r)
    print(" ")
    print("Account created successfully")
    print(" ")
    print("Kindly login to your new Amazon account")
    k=int(input("Type 1 to return home screen : "))
    if(k==1):
        os.system('cls')
        return usercheck()

def userhome(b):
    os.system('cls')
    print("Welcome",b['username'])
    print(" ")
    print("1) View Profile page")
    print("2) View all products")
    print("3) Search products")
    print("4) Compare products")
    print("5) Buy products")
    print("6) View cart")
    print("7) Cancel orders")
    print("8) Exit")

    q=int(input("Enter your choice : "))
    if(q==1):
        user_profile(b)
    elif(q==2):
        viewproduct(b)
    elif(q==3):
        search_product(b)
    elif(q==4):
        filterproduct(b)
    elif(q==5):
        buy_product(b)
    elif(q==6):
        cart_view(b)
    elif(q==7):
        cancel_order(b)
    elif(q==8):
        os.system('cls')
        usercheck()

def filterproduct(b):
    os.system('cls')
    w=input("Enter the product name to compare : ")
    print(" ")
    for i in merchant_product_list:
        if(i['product']==w):
            print("  Merchant id   : ",i['merchantid'],"          Total price     : ",i['productprice'])
            print("  Product Id    : ",i['productid'],"         Product name    : ",i['product'])
            print("  Discount      : ",i['productdiscount'],"           Discount amount : ",i['Discount Amount'])
            print("  Stock         : ",i['productstock'],"           Product price   : ",i['Discounted product price'])
            print("------------------------------------------------------------------------------------------")
            print(" ")
    
    print(" ")
    print("1) Price- Low to High")
    print("2) Price- High to Low")
    print(" ")
    kk=int(input("Enter your choice : "))
    if(kk==1):
        filter_lowtohigh(b,w)
    elif(kk==2):
        filter_hightolow(b,w)
    k=int(input("Type 1 to return home screen : "))
    if(k==1):
        os.system('cls')
        return userhome(b)

def filter_lowtohigh(b,w):
    os.system('cls')
    print("Products listed from low price to high price")
    print(" ")
    l11=[]
    for i in merchant_product_list:
        if(i['product']==w):
            l11.append(i)
    s_l=sorted(l11,key=itemgetter('Discounted product price'))
    for i in s_l:
        print("  Merchant id   : ",i['merchantid'],"          Total price     : ",i['productprice'])
        print("  Product Id    : ",i['productid'],"         Product name    : ",i['product'])
        print("  Discount      : ",i['productdiscount'],"           Discount amount : ",i['Discount Amount'])
        print("  Stock         : ",i['productstock'],"           Product price   : ",i['Discounted product price'])
        print("------------------------------------------------------------------------------------------")
        print(" ")
    print(" ")
    print("To buy a product type 1 [or] To return homescreen type 2")
    print(" ")
    k=int(input("Enter your choice : "))
    if(k==2):
        os.system('cls')
        return userhome(b)
    elif(k==1):
        buy_product(b)

def filter_hightolow(b,w):
    os.system('cls')
    print("Products listed from high price to low price")
    print(" ")
    l11=[]
    for i in merchant_product_list:
        if(i['product']==w):
            l11.append(i)
    s_l=sorted(l11,key=itemgetter('Discounted product price'),reverse=True)
    for i in s_l:
        print("  Merchant id   : ",i['merchantid'],"          Total price     : ",i['productprice'])
        print("  Product Id    : ",i['productid'],"         Product name    : ",i['product'])
        print("  Discount      : ",i['productdiscount'],"           Discount amount : ",i['Discount Amount'])
        print("  Stock         : ",i['productstock'],"           Product price   : ",i['Discounted product price'])
        print("------------------------------------------------------------------------------------------")
        print(" ")
    print("To buy a product type 1 [or] To return homescreen type 2")
    print(" ")
    k=int(input("Enter your choice : "))
    if(k==2):
        os.system('cls')
        return userhome(b)
    elif(k==1):
        buy_product(b)

def user_profile(b):
    os.system('cls')
    print("Welcome",b['username'])
    print(" ")
    print("Username     : ",b['username'])
    print("Userid       : ",b['userid'])
    print("________________________________")
    print(" ")
    print("1) View previous products that were brought")
    print("2) Card details")
    print("3) Update card details")
    print("4) Exit")
    print(" ")
    k=int(input("Enter your Choice : "))
    if(k==1):
        product_brought(b)
    elif(k==2):
        carddetails(b)
    elif(k==3):
        update_card(b)
    elif(k==4):
        os.system('cls')
        userhome(b)
    else:
        print("Invalid")
        return user_profile(b)

def cancel_order(b):
    os.system('cls')
    print("List of orders")
    print(" ")
    print("Welcome",b['username'])
    for i in product_history:
        if(i['userid']==b['userid']):
            print(" ")
            print("Merchant id              : ",i['merchantid'])
            print("Product name             : ",i['product'])
            print("Product id               : ",i['productid'])
            print("Amount                   : ",i['Discounted product price'])
            print("Product quantity         : ",i['productquantity'])
            print("Total price              : ",i['totalprice'])
            print(" ________________________________________________________")
            print(" ")
    w=int(input("Please enter the merchant id of a product : "))
    w1=int(input("Enter the product id : "))
    print(" ")
    for i in product_history:
        if((i['userid']==b['userid']) and (i['merchantid']==w) and (i['productid']==w1)):
            amount_of_user=i['totalprice']
            u=i['productquantity']
            s=int(input("Are you sure you want to cancel the order [If yes type 1] : "))
            if(s==1):
                for i in merchant_cardlist:
                    if(w==i['merchantid']):
                        i['productssold']=i['productssold']-u
                        print(i['productssold'])
                        i['balance']=i['balance']-amount_of_user
                        print(i['balance'])
                for i in merchant_product_list:
                    if((i['merchantid']==w) and (i['productid']==w1)):
                        i['productstock']=i['productstock']+u
                b['balance']=b['balance']+amount_of_user
                for i in product_history:
                    if((i['userid']==b['userid']) and (i['merchantid']==w) and (i['productid']==w1)):
                        product_history.remove(i)
        else:
            print("product not found")
            print(" ")
    k=int(input("Type 1 to return home screen : "))
    if(k==1):
        os.system('cls')
        return user_profile(b)
    
def product_brought(b):
    os.system('cls')
    print("List of products that were brought")
    print(" ")
    print("Welcome",b['username'])
    print(" ")
    for i in product_history:
        if(i['userid']==b['userid']):
            print(" ")
            print("Merchant id              : ",i['merchantid'])
            print("Product name             : ",i['product'])
            print("Product id               : ",i['productid'])
            print("Amount                   : ",i['Discounted product price'])
            print("Product quantity         : ",i['productquantity'])
            print("Total price              : ",i['totalprice'])
            print(" ________________________________________________________")
            print(" ")
    k=int(input("Type 1 to return home screen : "))
    if(k==1):
        os.system('cls')
        return user_profile(b)

def cart_view(b):
    os.system('cls')
    print("Cart details")
    for i in cart_add_list:
        print(" ")
        print("Merchant id              : ",i['merchantid'])
        print("Product name             : ",i['product'])
        print("Product id               : ",i['productid'])
        print("Price                    : ",i['productprice'])
        print("Discount                 : ",i['productdiscount'])
        print("Discount Amount          : ",i['Discount Amount'])
        print("Discounted Product price : ",i['Discounted product price'])
        print("Stock available          : ",i['productstock'])
        print(" ________________________________________________________")
        print(" ")
    print("1) Buy a product")
    print("2) Return to homescreen")
    print(" ")
    w=int(input("Enter your choice : "))
    if(w==1):
        buy_product(b)
    elif(w==2):
        os.system('cls')
        return userhome(b)

def update_card(b):
    os.system('cls')
    print("Welcome",b['username'])
    print(" ")
    print("Username          : ",b['username'])
    print("Userid            : ",b['userid'])
    print("Card holder name  : ",b['cardname'])
    print("Card number       : ",b['cardnumber'])
    print("Available balance : ",b['balance'])
    print(" ")
    print("_________________________________________")
    w=int(input("Enter the amount to be updated : "))
    for i in user:
        if(i['userid']==b['userid']):
            b['balance']=b['balance']+w
    print(" ")
    print("Balance updated successfully")
    print(" ")
    k=int(input("Type 1 to return home screen: "))
    if(k==1):
        os.system('cls')
        return user_profile(b)

def carddetails(b):
    os.system('cls')
    print("Welcome",b['username'])
    print(" ")
    print("Username          : ",b['username'])
    print("Userid            : ",b['userid'])
    print("Card holder name  : ",b['cardname'])
    print("Card number       : ",b['cardnumber'])
    print("Available balance : ",b['balance'])
    print(" ")
    k=int(input("Type 1 to return home screen: "))
    if(k==1):
        os.system('cls')
        return user_profile(b)

def search_product(b):
    os.system('cls')
    print("Welcome",b['username'])
    print(" ")
    name_of_product=input("Enter the product name to search : ")
    os.system('cls')
    print("Search results")
    for i in merchant_product_list:
        if(i['product']==name_of_product):
            print(" ")
            print("Merchant id              : ",i['merchantid'])
            print("Product name             : ",i['product'])
            print("Product id               : ",i['productid'])
            print("Price                    : ",i['productprice'])
            print("Discount                 : ",i['productdiscount'])
            print("Discount Amount          : ",i['Discount Amount'])
            print("Discounted Product price : ",i['Discounted product price'])
            print("Stock available          : ",i['productstock'])
            print(" ________________________________________________________")
            print(" ")
    print(" ")
    print("[If no products found, kindly check product name and return to homescreen. Else please enter your choice]")
    print(" ")
    print("1) Buy a product")
    print("2) Add the product to a cart")
    print("3) Return to homescreen")
    print(" ")
    w=int(input("Enter your choice : "))
    if(w==1):
        buy_product(b)
    elif(w==2):
        k=int(input("Enter the merchant id of a product to be added : "))
        u=int(input("Enter the product id : "))
        for i in merchant_product_list:
            if((i['merchantid']==k) and (i['productid']==u)):
                cart_add_list.append(i)
                os.system('cls')
                print("Product added to cart successfully")
                print("You can view the product details in view cart section")
                print(" ")
                log=int(input("To log out type 1: "))
                if(log==1):
                    return userhome(b)
    else:
        os.system('cls')
        return userhome(b)

def buy_product(b):
    os.system('cls')
    k=int(input("Enter the merchant id of a product to buy : "))
    q=int(input("Enter the product id : "))
    for i in merchant_product_list:
        if((i['merchantid']==k) and (i['productid']==q)):
            print(" ")
            print("Please confirm the details of the product before payment")
            print(" ")
            print("Merchant id              : ",i['merchantid'])
            print("Product name             : ",i['product'])
            print("Product id               : ",i['productid'])
            print("Price                    : ",i['productprice'])
            print("Discount                 : ",i['productdiscount'])
            print("Discount Amount          : ",i['Discount Amount'])
            print("Discounted Product price : ",i['Discounted product price'])
            print("Stock available          : ",i['productstock'])
    print("  ")
    print("1) Buy a product")
    print("2) Add the product to a cart")
    print("3) Return to homescreen")
    print(" ")
    w=int(input("Enter your choice : "))
    if(w==1):
        os.system('cls')
        print("Payment method")
        print("1) Card")
        l=int(input("Enter payment method : "))
        if(l==1):
            os.system('cls')
            card_number=int(input("Enter card number : "))
            card_name=input("Enter card holder name : ")
            print(" ")
            os.system('cls')
            if((b['cardnumber']==card_number) and (b['cardname']==card_name)):
                    print("Welcome",b['username'])
                    print(" ")
                    p=b['balance']
                    print("Your account available balance is",p)
                    print(" ")
                    for i in merchant_product_list:
                        if((i['merchantid']==k) and (i['productid']==q)):
                            qa=i['Discounted product price']
                            u=int(input("Enter the quantity of a product : "))
                            u1=i['productstock']
                            if(u>u1):
                                os.system('cls')
                                print("Not enough stock for a product")
                                print(" ")
                                ee=int(input("Enter 1 to return payment screen : "))
                                if(ee==1):
                                    os.system('cls')
                                    return buy_product(b)
                            else:
                                s=u*qa
                                if(p<s):
                                    os.system('cls')
                                    print("Not enough money in your wallet for payment")
                                    return userhome(b)
                                else:
                                    os.system('cls')
                                    print("Total price for productid",q,"is Rs.",s)
                                    for i in merchant_cardlist:
                                        if(k==i['merchantid']):
                                            i['productssold']=i['productssold']+u
                                            i['balance']=i['balance']+s
                                    print("Payment processing...")
                                    print(" ")
                                    yy=int(input("Enter your userid password : "))
                                    if(yy==b['userpassword']):
                                        os.system('cls')
                                        b['balance']=b['balance']-s
                                        print("Payment successfull")
                                        print(" ")
                                        print("The product will arrive to your location shortly")
                                        print(" ")
                                        for i in merchant_product_list:
                                            if((i['merchantid']==k) and (i['productid']==q)):
                                                a1=i['product']
                                        pp={'merchantid':k,'userid':b['userid'],'productid':q,'product':a1,'quantity':u,'amount':s}
                                        salesreport_list.append(pp)
                                        for i in cart_add_list:
                                            if((i['merchantid']==k) and (i['productid']==q)):
                                                cart_add_list.remove(i)
                                        useridd=b['userid']
                                        for i in merchant_product_list:
                                            if((i['merchantid']==k) and (i['productid']==q)):
                                                merchantid=i['merchantid']
                                                product=i['product']
                                                productidd=i['productid']
                                                amount=i['Discounted product price']
                                                i['productstock']=i['productstock']-u
                                        dd={'userid':useridd,'merchantid':merchantid,'product':product,'productid':productidd,'Discounted product price':amount,'productquantity':u,'totalprice':s}
                                        product_history.append(dd)
                                        log=int(input("To log out type 1 : "))
                                        if(log==1):
                                            return userhome(b)    
                    else:                                    
                        log=int(input("To log out type 1 : "))
                        if(log==1):
                            return userhome(b)
            else:
                os.system('cls')
                return userhome(b)
        else:
            os.system('cls')
            return userhome(b)
    elif(w==3):
        os.system('cls')
        return userhome(b)
    elif(w==2):
        cart_add_list.append(i)
        os.system('cls')
        print("Product added to cart successfully")
        print("You can view the product details in view cart section")
        print(" ")
        log=int(input("To log out type 1 : "))
        if(log==1):
            return userhome(b)

def viewproduct(b):
    os.system('cls')
    print("Welcome")
    print("List of products available in Amazon")
    print(" ")
    for i in merchant_product_list:
        print("  Merchant id   : ",i['merchantid'],"          Total price     : ",i['productprice'])
        print("  Product Id    : ",i['productid'],"         Product name    : ",i['product'])
        print("  Discount      : ",i['productdiscount'],"           Discount amount : ",i['Discount Amount'])
        print("  Stock         : ",i['productstock'],"           Product price   : ",i['Discounted product price'])
        print(" ")
        print("------------------------------------------------------------------------------------------")
        print(" ")
    print("To search a product type 1")
    print("       or         ")
    print("To exit to home screen type 2")
    print(" ")
    w=int(input("Enter your choice : "))
    if(w==1):
        search_product(b)
    else:
        os.system('cls')
        return userhome(b)

def useridgenerate():
    global userid
    userid=userid+1
    return userid

def usercheck():
    os.system('cls')
    print("Welcome to Amazon")
    print(" ")
    print("1) Existing user")
    print("2) New user. Create an Amazon account")
    print("3) Exit")
    print(" ")
    e=int(input("Please enter your choice : "))
    if(e==1):
        user_id_login()
    elif(e==2):
        user_id_create()
    elif(e==3):
        exitid()
    else:
        print("Invalid")
        return home()

def home():
    os.system('cls')
    print("Welcome to Amazon")
    print(" ")
    print("1) Admin login")
    print("2) Merchant login")
    print("3) User login")
    print("4) Exit")
    print(" ")
    n=int(input("Please Enter your choice : "))
    if(n==1):
        adminlogin()
    elif(n==2):
        merchantcheck()
    elif(n==3):
        usercheck()
    elif(n==4):
        exitportal()
    else:
        print("Invalid Input")
        return home()
home()