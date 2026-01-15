import sys
import random
import os
import json
from datetime import datetime

r = random.randint(1000,10000)
n = random.randint(1000,10000)

now = datetime.now()

date = now.strftime("%d-%m-%Y")
time = now.strftime("%H:%M")

product_order = []
product_price = []

next_user = {}

def sign_up():
    while True:
        try:
            with open("user_data.json","r") as f:
                user_data = json.load(f)   
        except:
            user_data = {}


        user_condition = input(" TO STOP TYPE(S) OR CONTINUE(C) =")
        

        if user_condition == "s" or user_condition == "S":
            break
        elif user_condition == "c" or user_condition == "C":

            #CONDITION FOR NAME            
            name = input("NAME =")
            
            if name.isdigit():
                print("PLASE USE A-Z ALPHABATE NOT NUMBERS")
                continue
            
            age = int(input("AGE ="))
            if age < 18:
                print("YOU ARE NOT ELEGIBLE....!")
                continue

            #CONDITION FOR PHONE.NO
            while True:

                phone = input("PHONE.NO =")
                if len(phone) == 10 and phone.isdigit():
                    break
                else:
                    print("PLEASE ENTER AN VALID PHONE NUMBER")
 
            #CONDITION FOR EMAIL
            while True:

                email = input("ENTER YOUR EMAIL =")

                exists = any(email in user for user in user_data.values())

                if "@" not in email:
                    print("PLEASE USE THIS @ SYMBOL ")
                    continue
                elif "gmail.com" not in email:
                    print("PLEASE USE THIS gmail.com IN YOUR EMAIL ")
                    continue
                elif exists:
                    print("EMAIL ALREADY EXISTS USE ANOTHER")
                elif email.isalpha() or email.isdigit():
                    print("PLEASE ENTER AN VALID EMAIL NOT AN INVALID")
                else:
                    os.system("cls")
                    break       

            #CONDITION FOR USERNAME
            while True:

                user_name = input('CREATE USERNAME =')
                if user_name in user_data:
                    print("ALREADY EXCITS USE DIFFIRENT USERNAME")
                    pass
                    continue
                else:
                    os.system("cls")
                    break

            #CONDITION FOR PASSWORD
            while True:
                password = input("CREATE PASSWORD  =")
                if password.isdigit() :
                    print("PLEASE USE A-Z ALPHABTE ALSO.......!")
                       
                elif password.isalpha():
                    print("USE 0-9 NUMBERS ALSO.........!")     
                elif "@" not in password and "#" not in password and "$" not in password and "%" not in password and "?" not in password and "&" not in password:
                    print("PLEASE USE THIS @, #, $, %, &, !, ?, SYMBOLS ALSO IN YOUR PASSWORD")

                else:
                    break
                    
            #NONE CONDITION FOR ADDRESS
            home_adress = input("HOME ADDRESS =")
 
            data_user =  {

                user_name :{
                    email:{

                    "NAME":name,
                    "AGE":age,
                    "PHONE.NO":phone,
                    "USERNAME":user_name,
                    "PASSWORD":password,
                    "EMAIL":email,
                    "HOME ADDRESS":home_adress

                    },
                },
            }

            user_data.update(data_user)
            next_user.update(data_user)
            with open("user_data.json","w") as f:
                json.dump(user_data, f, indent=4)  
    os.system("cls")
#LOGIN SYSTEM(FUNCTION)
def login_sys():
    with open("user_data.json","r") as f:
        data = json.load(f)

    attempt = 0
 
    while True:

        username = input("ENTER USERNAME =")
        
        if username in data:    
            break
        elif username not in data:
            print("THERE IS NONE ACCOUNT NAMED:",username,"PLEASE FIRST MAKE ACCOUNT")
            continue
        else:
            print("WRONG OR WRITE PROPERLY")
            return False
    email_key = list(data[username].keys())[0]
    check_pass = data[username][email_key]["PASSWORD"]

    while attempt < 3:
        password = input("ENTER PASSWORD =")
        if password == check_pass:
            print("SUCCESED TO LOGIN.......!")          
            print("WELCOME BACK",username.upper(),".......!")
            return True
        
        else:
            attempt += 1
            print("INCORRECT PASSWORD,", 3 - attempt,"ATTEMPT LEFT ")
        
    print("TOO MANY INCORRECT ATTEMPT RETRY IN SOME TIME..........!")
    os.system("cls")
    sys.exit()

#ORDER MANAGE SYSTEM (FUNCTION) 
def order_sys():
    with open("premium_data","r") as f:
        premium_c = json.load(f)
    
    with open("user_data.json","r") as f:
        data = json.load(f)

    try:
        with open("product_history.json","r") as f:
            history = json.load(f)
    except:
        history ={}
 
    product_list = {

        "smart tv":23000,
        "iphone 13":150000,
        "watch":3000,
        "tooth brush":30,

    }
    print("----------AVAILABLE PRODUCT----------\n")
    print("SMART TV = $23,000\n")
    print("IPHONE 13 = $1,50000\n")
    print("WATCH = $3,000\n")
    print("TOOTH BRUSH = $30\n")

    product_order = []
    product_price = []

    print("PLEASE......! WRITE PRODUCT NAME PROPERLY UDERVISE PRODUCT WILL NOT COUNT")

    while True:

      order = input("PRODUCT OR STOP[S]=")

      if order == "s" or order == "S":
          break
      elif order in product_list:
          product_order.append(order)
          product_price.append(product_list[order])

    Sum = sum(product_price)
    new_addres = "NONE"

    new_p = "NONE"
    new_p = Sum / 20

    user_name_c = input("YOUR USERNAME :")
    
    if user_name_c in data:
         d_addres = input("DELIVERY ADDRES :")
         print(user_name_c.upper(),"CONGRATES YOUR ORDER",product_order, "IS COMFIRMED YOUR TOTAL BILL IS ","$",Sum,",YOUR ORDER ID :",r,"AND YOUR DELIVERY ADDRESS IS",d_addres.upper())
         order_c = input("ONLY FOR CONFORMATION IF YOU WANT TO CHANGE DELIVERY ADDRESS[C] OR IF YOU DON'T WANT TO CHANGE[D]  :")
         
         if order_c == "d" or order_c == "D":
             print("THANKS......! FOR YOUR RESPONSE")

         elif order_c == "c" or order_c == "C":
             new_addres = input("YOUR NEW ADDRES :")
             print(user_name_c.upper(),"CONGRATES YOUR ORDER",product_order, "IS COMFIRMED YOUR TOTAL BILL IS ","$",Sum,",YOUR ORDER ID :",r,"AND YOUR DELIVERY ADDRESS IS",new_addres.upper())
             print("THANKS......! FOR YOUR RESPONSE")
         check_premium = input("ENTER YOUR PREMIUM PIN OR DON'T HAVE[D] :")
         if check_premium == "d" or check_premium == "D":
             sys.exit()
         elif check_premium in premium_c:
             print("SUCCESS YOUR PIN IS RIGHT")
             print(user_name_c.upper(),"CONGRATES YOUR ORDER",product_order, "IS COMFIRMED YOUR TOTAL BILL IS ","$",new_p,",YOUR ORDER ID :",r,"AND YOUR DELIVERY ADDRESS IS",new_addres.upper())
             print("THANKS......! FOR YOUR RESPONSE")
         elif check_premium not in premium_c:
             print("WRONG PIN OR FIRST MAKE PREMIUM ACCOUNT FOR EXTRA DISCOUNT ")
         elif check_premium == "":
             print("WE CAN'T ACCEPT AN EMPTY PIN PLEASE....! FILL IT")
         else :
             print("PLEASE...! CHOICE RIGHT OPTION DON'T WRITE ANYTHING")

    else:
        print("YOUR NAME IS WRONG OR PLEASE....! FIRST DO SIGN UP FOR ORDER")
        
    
    product_data = {
        r:{    

            "USERNAME":user_name_c,
            "OLD DELIVERY ADDRESS":d_addres,
            "NEW DELIVERY ADDRESS":new_addres,
            "PRODUCT LIST":product_order,
            "TOTAL BILL":Sum,
            "TOTAL BILL WITH DISCOUNT":new_p,
            "ORDER ID":r,
            "ORDER-DATE":date,
            "ORDER-TIME":time,

        },
    }
    

    history.update(product_data)

    with open("product_history.json","w") as f:
        json.dump(history,f,indent=4)
    
       
def product_h():
    with open("product_history.json","r") as f:
        history_data = json.load(f)

    while True:

        user_choice = input("TO SEE HISTORY[H] OR DON'T WANT TO SEE[D] :")

        if user_choice == "d" or user_choice == "D":
            print("THANKS....! FOR COMING")
            break
        elif user_choice == "h" or user_choice == "H":

            while True:
                order_id = input("ENTER YOUR ORDER ID OR STOP[1] :")

                if order_id == "1":
                    print("THANKS....! FOR COMING")
                    break
                elif order_id == "":
                    print("EMPTY ID CANNOT BE ACCEPTED PLEASE......! WRITE ORDER ID")
                elif order_id.isalpha():
                    print("PLEASE....! ENTER ONLY NUMBER NOT ALPHABET")
                elif order_id.isdigit():
                    os.system("cls")
                    if order_id in history_data:
                        for s, e in history_data[order_id].items():
                            print(s, " = " , e)
                    elif order_id not in history_data:
                        print("THERE IS NOT ANY BILL IN HISTORY OF THIS",order_id,"ORDER ID")
        
        elif user_choice.isdigit():
            print('PLEASE....! WRITE ALPHABETS ONLY NOT NUMBER')
        else:
            print("PLEASE.....! CHOOSE CORRECT OPTION")

#PRIMIUM ACC MAGAMENT
def primium_acc():
    p = random.randrange(1,10000)
    with open("user_data.json","r") as f:
        user = json.load(f)  

    try:
        with open("premium_data.json","r") as f:
           pre_data = json.load(f)
    except:
        pre_data = {}  

    while True:
        premium = input("TO MAKE YOUR ACCOUNT PREIMIUM[1] OR STOP[2] :")

        if premium == "1" :
            while True:

                p_username = input("ENTER YOUR USERNAME OR STOP[R] :")
                if p_username == "r" or p_username == "R":
                    break            
                elif p_username in user:
                    data_user = p_username
                    while True:

                        acc_no = input('ENTER YOUR 12 DIGIT ACC.NO :')
                        if acc_no.isalpha():
                            print("PLEASE.....! ENTER NUMBER ONLY NOT ALPHABETS")
                        elif acc_no == "":
                            print("WE CAN'T ACCEPT AN EMPTY ACC.NO PLEASE...! ENTER ACC.NO")
                        elif acc_no.isdigit() and len(acc_no) == 12:
                            os.system("cls")
                            print("YOUR PAYMENT HAS SUCCESSFULLY DONE.....!")
                            print("YOUR ACC CONVERTED TO PREMIUM YOUR PREMIUM PIN IS",p)
                            break
                        else:
                            print("PLEASE.....! ENTER YOUR 12 DIGIT ACCOUNT NUMBER DON'T WRITE ANYTHING")
                elif p_username not in user:
                    print("WE CAN'T FIND AN ACCOUNT PLEASE....! D SIGN UP")
                elif p_username.isdigit():
                    print("PLEASE.....! ENTER ALPHABETS ONLY NOT ANY ELSE")
                elif p_username == "":
                    print("WE CAN'T ACCEPT AN EMPTY USERNAME PLEASE...! ENTER USERNAME")
                    
                
        elif premium == "":
            print("WE CAN'T ACCEPT AN EMPTY OPTION PLEASE...! ENTER YOUR CHOICE")
        elif premium.isalpha():
            print("PLEASE.....! ENTER NUMBER ONLY NOT ALPHABETS")
        elif premium == "2":
           break
        else:
            print('WRONG CHOICE PLEASE.....! CHOOSE AN RIGHT OPTION NOT ANYTHING')

        premium_acc_data = {
            p:{
                "ACCOUNT.NO":acc_no,
                "USERNAME":data_user,
                "DATE":date,
                "TIME":time,
        },
    }
    
    pre_data.update(premium_acc_data)
    with open("premium_data.json","w") as f:
        json.dump(pre_data,f,indent=4)

#FINAL WORKING CODE
while True:
    print("----------WELCOME TO POWERED-SEYAN ORDER CO-OP----------")
    print("SIGN UP = 1")
    print("LOGIN = 2")
    print("PREMIUM ACCOUNT CONVERTION = 3")
    print("ORDER PRODUCT = 4")
    print("ORDER HISTORY = 5")
    print("EXIT = 6")


    user_c = input("YOUR CHOICE :")
    if user_c == "6":
        print("THANKS....! FOR COMING")
        print("EXITING........")
        break
    elif user_c == "1":
        sign_up()
        os.system("cls")
    elif user_c == "2":
        login_sys()
        os.system("cls")
    elif user_c == "3":
        primium_acc()
        os.system("cls")
    elif user_c == "4":
        order_sys()
        os.system("cls")
    elif user_c == "5":
        product_h()
        os.system("cls")
    elif user_c.isalpha():
        print("ONLY NUMBER'S ARE ALLOWED NOT ALPHABETS")
        os.system("cls")
    else:
        print("PLEASE.......! CHOOSE AN CORRECT OPRION")
        os.system("cls")
