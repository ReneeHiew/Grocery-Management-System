#Hiew En Xin Renee
#TP064210
'''
Admin
'''
username_list = [ ]

#function to add new admin username
def add_admin_username( ):
    adminfile=open('adminsystem.txt' , 'r') 
    new_username=input(str("Enter new username: ")).lower()
    username_list.append(new_username.lower())
    print("New admin added successfully.")

    adminfile = open('adminsystem.txt' , 'a')
    adminfile.write(new_username.lower() + "\n")
    adminfile.close( )

#function for admin to login to admin system
def admin( ):
    adminfile=open('adminsystem.txt' , 'r')
    admin_username=input(str("Enter admin username: ")).lower()
    adminlines = adminfile.readlines()
    for line in adminlines:
        line=line.strip()
        if not admin_username.lower() in line.lower():
            continue
        print(line + ", user found. Please enter admin password.")
        admin_password( )
        break
    else:
        print("User not found, kindly try again.")
        admin()
 
    adminfile.close( )
    
#function that was combined into the admin function    
def admin_password( ):
    admin_password=input(str("Enter admin password: "))
    if admin_password=="101417":
        print("Welcome to FRESHCO Sdn Bhd admin system.")
        admin_menu( )
    else:
        print("Incorrect password, kindly try again.")
        admin( )

#function to guide and allow admin to decide and operate what they want to do
def admin_menu( ):
    while True:
        print("What would you like to operate? Please insert the number based on the desciption provided")
        print("Insert number 1 to  view all groceries.")
        print("Insert number 2 to upload new groceries.")
        print("Insert number 3 to search for certain grocery.")
        print("Insert number 4 to delete grocery.")
        print("Insert number 5 to  update groceries.")
        print("Insert number 6 to view all customer orders.")
        print("Insert number 7 to search certain customer orders.")
        print("Insert number 8 to add new admin username.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                view_groceries( )
                exit_admin_system( )
                break
            elif(selection==2):
                upload_groceries( )
                exit_admin_system( )
                break 
            elif(selection==3):
                search_groceries( )
                exit_admin_system( )
                break
            elif(selection==4):
                delete_groceries( )
                exit_admin_system( )
                break
            elif(selection==5):
                update_groceries_menu( )
                exit_admin_system( )
                break 
            elif(selection==6):
                view_all_customer_order( )
                exit_admin_system( )
                break
            elif(selection==7):
                view_customer_order( )
                exit_admin_system( )
                break
            elif(selection==8):
                add_admin_username( )
                exit_admin_system( )
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            admin_menu( )
            break
    
    
groceries_list = [ ]
new_groceries_list = [ ]

#function to upload new groceries into grocery system
def upload_groceries( ):
    grocery_code = input(str("Enter code of grocery: "))
    code=int(grocery_code)
    for groceries in range(code):
        groceries_brandname = input(str("Enter grocery brandname: ")).lower()
        new_groceries_list.append(groceries_brandname.lower())
        groceries_details = input(str("Enter grocery detail(category): ")).lower()
        new_groceries_list.append(groceries_details.lower())
        grocery_expired_dte = input(str("Enter grocery expired date: ")).lower()
        new_groceries_list.append(grocery_expired_date.lower())
        grocery_price = input(str("Enter grocery price: ")).lower()
        new_groceries_list.append(grocery_price.lower())
        groceries_list.append(new_groceries_list)
        groceryfile = open('grocerysystem.txt' , 'a')
        groceryfile.write("\n" + grocery_code + "|" + groceries_brandname + ", " + groceries_details + ", " + grocery_expired_date + ", " + grocery_price + "\n")
        groceryfile.close( )
        print("Upload Successful")
        break
    return groceries_list  

#function to search for groceries in rocery system 
def search_groceries( ):
    groceryfile = open('grocerysystem.txt' , 'r')
    grocerylines = groceryfile.readlines()
    print("What would you like to search?")
    search=input("Insert item: ").lower()
    for item in grocerylines:
        if not search.lower() in item:
            continue
        print(item)
        break
    else:
        print("Item not found.")

    groceryfile.close( )

#function to view all groceries in the grocery system 
def view_groceries( ):
    groceryfile = open('grocerysystem.txt' , 'r')
    grocerylines = groceryfile.readlines()
    print("Welcome and thank you for using our FRESHCO Sdn Bhd grocery system.")
    for item in grocerylines:
        item=item.strip()
        print(item)
        
    groceryfile.close( )

#function for admin to decide to either stay or exit the system
def exit_admin_system( ):
    while True:
        print("Insert number 1 to stay in admin system.")
        print("Insert number 2 to go back to grocery system main page.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                admin_menu( )
                break
            else:
                system_main_page( )
                print("Thank you and have a nice day.")
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            exit_admin_system( )

order_list=[ ]

#function for customer to make orders
def customer_order( ):
    username=input("Enter username: ").lower()
    print("Hi, " + username + ". " + "What would you like to make an order?")
    order=input("Enter grocery code: ")
    groceryfile = open('grocerysystem.txt' , 'r')
    grocerylines = groceryfile.readlines()
    for item in grocerylines:
        if item.startswith(order):
            print(item)
            order_list.append(item)
            for order in order_list:
                customerfile = open('customerorder.txt' , 'a')
                customerfile.write(username + ": " + order + "\n")
                customerfile.close( )
            add_order()
            break
    else:
        print("Invalid grocery code, please try again.")
        customer_order()

    groceryfile.close( )
   
#function combined with the previous function
def add_order( ):
    print("Would you like to add other items into your order?")
    print("Insert number 1 to add other item.")
    print("Insert number 2 to checkout.")
    choice=int(input("Enter number: "))
    if choice!=1:
        print(order_list)
        print("Thank you for shopping with FRESHCO!")
        print("Payment method: Credit and Debit Card/Cash on Delivery. Kindly enter 'Card' for Credit/Debit Card and 'Cash' for Cash on Delivery.")
        payment=input("Payment method: ").lower()
        if payment.lower()=='card':
            cardnum=input("Enter Credit/Debit Card Number: ")
            cardpassword=input("Enter card password: ")
            cardexp=input("Enter card expire date (MM/YY): ")
            cardpin=input("Enter card cvv (3 Digit): ")
            print("Payment Successful")
            print("FRESHCO will be sending your groceries to your doorstep ASAP, we appreciate your time and patients. Thank You!")
        else:
            print("Kindly make payment to our staff while receiving your groceries.")
            print("FRESHCO will be sending your groceries to your doorstep ASAP, we appreciate your time and patients. Thank You!" )
    else:
        print("Thank you for choosing us, proceeding to grocery cart.")
        customer_order()

#function for admin to view all customer order
def view_all_customer_order( ):
    customerfile = open('customerorder.txt' , 'r')
    customerlines = customerfile.readlines()
    for item in customerlines:
        item=item.strip()
        print(item)

    customerfile.close( )

#function admin to search for specific order and customer to view their own orders
def view_customer_order():
    customerfile = open('customerorder.txt', 'r')
    customerorder = customerfile.read()
    customerfile.close()
    customerusername = input("Enter customer username: ").lower()
    if customerusername not in customerorder:
        print("No order found for this username.")
    
    elif customerusername in customerorder:
        customerfile = open('customerorder.txt', 'r')
        customerlines = customerfile.readlines()
        customerfile.close()
        for item in customerlines:
            item = item.strip()
            if item.startswith(customerusername):
                print(item)
    else:
        print("No order found for this username.")

#function for admin to delete groceries in the system
def delete_groceries( ):
    delete =  input('Enter delete item: ')
    groceryfile = open('grocerysystem.txt', 'r')
    grocerylines = groceryfile.readlines()
    groceryfile.close()  
    confirmation = input("Confirm delete item?").lower()
    if confirmation.lower()=='yes':
        groceryfile = open('grocerysystem.txt','w')
        for item in grocerylines:
            if delete not in item:
                groceryfile.write(item)
        groceryfile.close()
        print("Item deleted.")
    else:
        print("Item not deleted.")
        
#function for admin to change grocery details
def update_groceries( ):
    original=str(input("Enter current data: ")).lower()
    replacement=str(input("Enter new data: ")).lower()
    groceryfile = open('grocerysystem.txt' , 'r')
    grocerylines = groceryfile.readlines()
    groceryfile.close()
    confirmation = input("Confirm update item?").lower()
    if confirmation.lower()=='yes':
        groceryfile = open('grocerysystem.txt' , 'w')
        for line in grocerylines:
            line=line.replace(original.lower(), replacement.lower())
            groceryfile.write(line)
        groceryfile.close()
        print("Grocery updated.")
    else:
        print("Grocery not updated.")
   

#function to guide admin in which section they want to change
def update_groceries_menu( ):
    while True:
        print("Which section of grocery would you like to update?")
        print("Insert number 1 to change grocery brandname.")
        print("Insert number 2 to change grocery details(category).")
        print("Insert number 3 to change grocery expired date.")
        print("Insert number 4 to change grocery price.")
        try:
            choice=int(input("Enter number: "))
            if(choice==1):
                update_groceries( )
                break
            elif(choice==2):
                update_groceries( )
                break
            elif(choice==3):
                update_groceries( )
                break
            elif(choice==4):
                update_groceries( )
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            update_groceries_menu( )

'''
Customer
'''

customer_list=[ ]
customer_detail_list=[ ]

#function for new customers to make registration
def new_customer( ):
    while True:
        print("Kindly fill your personal details for registration, user must fill in all section to register successfully.")
        customer_username=input(str("Create username: ")).lower()
        customer_detail_list.append(customer_username.lower())
        customer_address=input(str("Enter address: ")).lower()
        customer_detail_list.append(customer_address.lower())
        customer_email=input(str("Enter e-mail address: ")).lower()
        customer_detail_list.append(customer_email.lower())
        customer_contactnum=input(str("Enter contact number: "))
        contactnum=int(customer_contactnum)
        customer_detail_list.append(customer_contactnum)
        customer_gender=input(str("Enter gender: ")).lower()
        customer_detail_list.append(customer_gender.lower())
        customer_dob=input(str("Enter date of birth (DD/MM/YY): ")).lower()
        customer_detail_list.append(customer_dob.lower())
        customer_password=input(str("Create password: "))
        if len(customer_password)==4:
            customer_detail_list.append(customer_password)
        elif len(customer_password)<4:
            print("Password too short, kindly try again.")
            new_customer()
            break
        else:
            print("Password too long, kindly try again.")
            new_customer()
            break
        customer_list.append(customer_detail_list)
        customerfile = open('customerdata.txt' , 'a')
        customerfile.write(customer_username + "|" + customer_address + ", " + customer_email + ", " + customer_contactnum + ", " + customer_gender + ", " + customer_dob + ", " + customer_password + "\n")
        customerfile.close( )
        print("Registration Successful. Kindly log in as registered customer.")
        break

#function for registered customer to login to grocery system 
def register_customer( ):
    customerfile = open('customerdata.txt' , 'r')
    username=input(str("Enter username: ")).lower()
    customerlines = customerfile.readlines()
    for line in customerlines:
        line=line.strip()
        if not username.lower() in line:
            continue
        print(username + ", user found. Please enter username password.")
        register_customer_password( )
        break
    else:
        print("User not found, kindly register yourself.")
        new_customer()

    customerfile.close( )

#function combined to the previous function
def register_customer_password( ):
    customerfile = open('customerdata.txt' , 'r')
    password=input(str("Enter username password: "))
    customerlines = customerfile.readlines()
    for line in customerlines:
        line=line.strip()
        if not password.lower() in line:
            continue
        print("Login successful, welcome to FRESHCO Sdn Bhd grocery system.")
        customer_menu( )
        break
    else:
        print("Incorrect password, kindly try again.")
        register_customer_password()

    customerfile.close( )

#function for customer to view their own profile
def view_customer_profile( ):
    customerfile = open('customerdata.txt' , 'r')
    customerusername=input(str("Enter username: ")).lower()
    customerlines = customerfile.readlines()
    for line in customerlines:
        line=line.strip()
        if not line.startswith(customerusername):
            continue
        print(line)
        break
    else:
        print("User not found, please try again.")
        view_customer_profile( )
        
    customerfile.close( )

#function for to guide and allow customer to choose what they want to do
def customer_menu( ):
    while True:
        print("What would you like to operate? Please insert the number based on the desciption provided")
        print("Insert number 1 to  view all groceries.")
        print("Insert number 2 to place order.")
        print("Insert number 3 to view own order.")
        print("Insert number 4 to view profile.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                view_groceries( )
                exit_customer_system( )
                break
            elif(selection==2):
                customer_order( )
                exit_customer_system( )
                break 
            elif(selection==3):
                view_customer_order( )
                exit_customer_system( )
                break
            elif(selection==4):
                view_customer_profile( )
                exit_customer_system( )
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            customer_menu( )
            break

#function to guide and allow new customers to choose what they want to do
def new_customer_menu( ):
    while True:
        print("What would you like to operate? Please insert the number based on the desciption provided")
        print("Insert number 1 to  view all groceries.")
        print("Insert number 2 to register.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                view_groceries( )
                print("Please register to enable more features!")
                new_customer_menu( )
                break
            elif(selection==2):
                new_customer( )
                break 
        except:
            print("Kindly try again by inserting a number following the description provided.")
            new_customer_menu( )
            break

#function for admin to decide to either stay or exit the system
def exit_customer_system( ):
    while True:
        print("Insert number 1 to stay in customer system.")
        print("Insert number 2 to go back to grocery system main page.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                customer_menu( )
                break
            else:
                system_main_page( )
                print("Thank you and have a nice day.")
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            exit_customer_system( )
            break

'''
Grocery System
'''
#function to return to the main page of grocery system 
def system_main_page( ):
    while True:
        print("____________________________Welcome to FRESHCO Sdn Bhd Grocery System________________________________")
        print("Kindly select and insert the number based on the description that was provided.")
        print("Kindly insert number 1 if you are an admin.")
        print("Kindly insert number 2 for registered customer.")
        print("Kindly insert number 3 for new customers.")
        print("Kindly insert number 4 to exit this grocery system.")
        try:
            selection=int(input("Insert number: "))
            if(selection==1):
                admin( )
                break
            elif(selection==2):
                register_customer( )
                break 
            elif(selection==3):
                new_customer_menu( )
                break
            elif(selection==4):
                print("Thank you for visiting FRESHCO Grocey System, have a nice day and see you again.")
                break
        except:
            print("Kindly try again by inserting a number following the description provided.")
            system_main_page( )
            break


'''
FRESHCO Grocery System
'''
while True:
    print("____________________________Welcome to FRESHCO Sdn Bhd Grocery System________________________________")
    print("Kindly select and insert the number based on the description that was provided.")
    print("Kindly insert number 1 if you are an admin.")
    print("Kindly insert number 2 for registered customer.")
    print("Kindly insert number 3 for new customers.")
    print("Kindly insert number 4 to exit this grocery system.")
    try:
        selection=int(input("Insert number: "))
        if(selection==1):
            admin( )
            break
        elif(selection==2):
            register_customer( )
            break 
        elif(selection==3):
            new_customer_menu( )
            break
        elif(selection==4):
            print("Thank you for visiting FRESHCO Grocey System, have a nice day and see you again.")
            break
    except:
        print("Kindly try again by inserting a number following the description provided.")
        




            
    
        
   
        
    
                                            
    

    
            


