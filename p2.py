def Admin():
    username=input("Please enter username ")
    password=int(input("Please enter password "))

    if username=='Devanshu' and password==5432 :
        Admin_portal()

    else:
        print("Invalid Credentials")

def Add_customer():
    print("Please Enter the following details :")
    Name=input("Enter Your name ")
    Age=int(input("Enter Your age "))
    Pan=input("Enter Your pan number ")
    print("Customer added !")
    with open('Customer.txt','a') as f:
        f.write(f"{Name} , {Age} , {Pan}\n" )
    Admin_portal()


def Add_bike_owner():
    print("Please Enter the following details :")
    Name=input("Enter Your name ")
    Age=int(input("Enter Your age "))
    Pan=input("Enter Your pan number ")
    print("Bike owner added !")
    with open('Bike_owner.txt','a') as f:
        f.write(f"{Name} , {Age} , {Pan}\n" )
    Admin_portal()

def Admin_portal():
    print("Welcome Sir!")
    print("Please select from given options:")
    print("1. Add customer ")
    print("2. Add bike owner ")
    print("3. Main menu ")
    print("4. Exit ")

    try:
        choice=int(input("Please Enter Your choice :"))

    except:
        print((""))
        print(("Invalid choice!! Please try again"))
        run()
    if choice==1:
        Add_customer()
    elif choice==2:
        Add_bike_owner()
    elif choice==3:
        run()
    elif choice==4:
        exit()
    else:
        print("Invalid choice!! Please try again")


def Bikes():
    with open('Bike_Specks.txt','r') as f:
        print(f.read())
        Customer_portal()
def Rent_bike():
    Model=input("Please Enter the model number of Bike that you want :")
    Interval=int(input("Enter 1 for Daily\n2 for weekly\n3 for Monthly timeperiod "))
    if Model=='B01':
        if Interval==1:
            print("Your Rent is 100 Rs ")
        elif Interval==2:
            print("Your Rent is 500 Rs ")
        else:
            print("Your Rent is 1500 Rs ")
    elif Model=='B02':
        if Interval==1:
            print("Your Rent is 100 Rs ")
        elif Interval==2:
            print("Your Rent is 400 Rs ")
        else:
            print("Your Rent is 1200 Rs ")
    elif Model=='B03':
        if Interval==1:
            print("Your Rent is 80 Rs ")
        elif Interval==2:
            print("Your Rent is 350 Rs ")
        else:
            print("Your Rent is 1000 Rs ")
    else:
        if Interval==1:
            print("Your Rent is 80 Rs ")
        elif Interval==2:
            print("Your Rent is 320 Rs ")
        else:
            print("Your Rent is 800 Rs ")
    print("Please Proceed for Payment")
    print("Thank you for using our service...")
    



def Return_Bike():
    try:
        choice=input("Please Enter the model number of Bike that you want to return :")
    except:
        print((""))
        print(("Invalid choice!! Please try again"))
        run()
    if choice=='B01':
        {
            print("You are using KTM RC 200\n We hope you like our services")
        }
    elif choice=='B02':
        {
            print("You are using Royal Enfield Bullet 350\n We hope you like our services")
        }
    elif choice=='B03':
        {
            print("You are using TVS Apache RTR 160 4V\n We hope you like our services")
        }
    elif choice=='B04':
        {
            print("You are using Bajaj Pulsar 150\n We hope you like our services")

        }
    elif choice=='B05':
        {
            print("You are using Hero Splendor Plus\n We hope you like our services")  
        }
    else:
        print("Invalid choice!! Please try again")
    print("Bike returned Sucessfully")
    print("Thank You for using our services.\n Have a nice Day...")
    

def Customer_portal():
    print("Please select from given options:")
    print("1. Available Bikes")
    print("2. Rent Bike")
    print("3. Returned Bike")
    print("4. Main Menu")
    print("5. Exit")

    try:
        choice=int(input("Please Enter Your choice : "))

    except:
        print((""))
        print(("Invalid choice!! Please try again"))
        run()
    if choice==1:
        Bikes()
    elif choice==2:
        Rent_bike()
    elif choice==3:
        Return_Bike()
    elif choice==4:
        Customer_portal()
    elif choice==5:
        exit()
    else:
        print("Invalid choice!! Please try again")



def Add_Bike():
    print("Enter the following details separated by a space and ',' ")
    Name,Mdl_no,Cc,Abs,D,W,M=input("Enter name, model number, Cc, Abs,Daily,weekly and monthly rent  ").split(",")
    with open('Bike_Specks.txt','a') as f:
        arg=(f"\n{Name} {Mdl_no} {Cc} {Abs} {D} {W} {M}")
        f.write(arg)
    print("Bike added  successfully !")
    Bike_owner_portal()

def Remove_bike():
    with open('Bike_Specks.txt','r') as f:
        print(f.read())
    a=open('Bike_Specks.txt')
    lines=a.readlines()
    a.close()
    l=int(input("Enter the line you want to remove "))
    del lines[l]

    b=open('Bike_Specks.txt','w')
    for line in lines:
        b.write(line)

    b.close()
    print("Bike Remove successfully !")
    Bike_owner_portal()


def Bike_owner_portal():
    print("Please select from given options:")
    print("1. Add Bike")
    print("2. Remove Bike")
    print("3.Exit")
    try:
        choice=int(input("Please Enter Your choice : "))

    except:
        print((""))
        print(("Invalid choice!! Please try again"))
        run()
    if choice==1:
        Add_Bike()
    elif choice==2:
        Remove_bike()
    elif choice==3:
        exit()
    else:
        print("Invalid choice!! Please try again")



def run():
    print("Please select from given options:")
    print("1. Admin's Portal")
    print("2. Custemer's Portal")
    print("3. Bike Owner's Portal")
    print("4. Exit")

    try:
        choice=int(input("Please Enter Your choice : "))

    except:
        print((""))
        print(("Invalid choice!! Please try again"))
        run()
    if choice==1:
        Admin()
    elif choice==2:
        Customer_portal()
    elif choice==3:
        Bike_owner_portal()
    elif choice==4:
        exit()
    else:
        print("Invalid choice!! Please try again")



run()

    