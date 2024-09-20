bank ={}

def write_file():
    global bank
    f = open("data.txt","w")
    for name,(username,password,money) in bank.items():
        f.write(f"{name},{username},{password},{(money)}\n")

def signUp():
    global bank
    name = input("Enter Your Name:-\t")
    username = input("Enter Your Username:-\t")
    password = input("Create Your Password:-\t")
    money = 0 

    

    bank[name] = [username,password,money]
    print("Your Account Has Been Created...!!!")
    write_file()
    return name


def login():
    global bank
    namee = input("Enter Your Registered Name:-\t")
    username = input("Enter Your Registered Usrename:-\t")
    password = input("Enter Your Password:-\t")

    if namee in bank and username == bank[namee][0] and password == bank[namee][1]:
        print("Login Sucessful..!!")
        return namee
    else:
        print("Something Went Wrong Try Again")

def transaction(name):
    global bank
    money = bank[name][2]
    operation = input("Enter The Operation You Want To Do?\t")
    amount = int(input(f"Enter The Amount Of Money You Want To {operation}:-\t"))

    if(operation.lower()=="withdraw"):
        if(money == 0):
            print("OOPs Empty Balance...!!!")
        elif(money<amount):
            print("Not Enough Balance")
        else:
            money = money - amount
            print(f"The Amount Of {amount} has been withdrawn from your account")

    elif(operation.lower() == "deposit"):
        money = money + amount
        print(f"The Amount Of {amount} has been deposited in your account")

    bank[name][2] = money
    write_file()

def view(name):
    x = input("Are You Admin Or User?\t")

    if(x.lower()=="admin"):
        print(bank)

    elif(x.lower()=="user"):
        print(f"Name = {name}\nUsername = {bank[name][0]}\nCurrent Balance = {bank[name][2]}")




def read_data():
    global bank
    f = open("data.txt","r")

    for line in f:
        name,username,password,money = line.strip().split(',')
        bank[name] = [username,password,int(money)]



print("Welcome To Rivu's Bank\n")

read_data()

user_action = input("Do You Want To Login Or Create A New Account? ").lower()

if user_action == "login":
    logged_in_user = login()
    if logged_in_user:
        operation = input("What operation do you want to do (transaction/view)? ").lower()
        if operation == "transaction":
            transaction(logged_in_user)
        elif operation == "view":
            view(logged_in_user)

elif user_action == "create":
    signUp()



    






        







