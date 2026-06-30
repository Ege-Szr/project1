import re
from database import add_account,update_account,delete_account,show_users_information
import time


def My_Sign_Up():
          
    try:
        account_mail=input("Email address: ")
        account_password=input("Password: ")

        if len(account_mail)<=10 or "@" not in account_mail:
            exception=Exception("Email address is incomplete")
            raise exception
            
        else:
            mail_pattern=r"^[a-zA-Z0-9.,?+-]+@[a-z]+\.[a-z]{2,3}$"
                
            if re.fullmatch(mail_pattern,account_mail):
                print("Email address is acceptable")

            else:
                exception=Exception("Email address is unaccaptable")
                raise exception
                
            if len(account_password)<3:
                exception=Exception("It should be at least 3 characters")
                raise exception
            else:
                password_pattern=r"[a-zA-Z0-9!#-_*<>$]{3,}"
                if re.fullmatch(password_pattern,account_password):
                    print("Password is acceptable")
                else:
                    exception=Exception("password is unacceptable")
                    raise exception
            print("account created")
            return add_account(account_mail,account_password)
    except Exception as e:
        print(e)

def My_Sign_In():
    mail=input("Email address: ")
    password=input("Password: ")
    result=show_users_information(mail,password)

    return result


while True:
    print("------WELCOME TO THE MENU------")
    print("Enter 1 to sign up")
    print("Enter 2 to sign in")
    print("Enter 3 to update account")
    print("Enter 4 to delete account")
    print("Enter 5 to show user information:")
    print("Enter 6 to exit")
    choice=input("Please enter your choice: ")

    if choice=="1":
        My_Sign_Up()
        
    elif choice=="2":
        print(My_Sign_In())

    elif choice=="3":
        now_mail=input("Email address:")
        now_password=input("Password:")
        result=show_users_information(now_mail,now_password)


        if "were found" in result:
            print("------WELCOME TO THE UPDATE MENU------")
            print("Enter 1 to update email address:")
            print("Enter 2 to update password: ")
            print("Enter 3 to update both of them:")
            print("Enter 4 to return")
            choice=input("Please enter your choice:")

            mail_pattern=r"^[a-zA-Z0-9.,?+-]+@[a-z]+\.[a-z]{2,3}$"
            password_pattern=r"[a-zA-Z0-9!#-_*<>$]{3,}"

            if choice=="1":
                new_mail=input("Enter new email address:")
                if re.fullmatch(mail_pattern,new_mail) and len(new_mail)>=10:
                    print(update_account(now_mail,now_password,new_mail,None))
                else:
                    print("Sorry, email address information could not be updated")
 
            elif choice=="2":
                new_password=input("Enter new password:")
                if re.fullmatch(password_pattern,new_password):
                    print(update_account(now_mail,now_password,None,new_password))
                else:
                    print("Sorry, password information could not be updated")

            elif choice=="3":
                new_mail=input("Enter new email address:")
                new_password=input("Enter new pasword:")
                if re.fullmatch(mail_pattern,new_mail) and re.fullmatch(password_pattern,new_password) and len(new_password)>=3:
                    print(update_account(now_mail,now_password,new_mail,new_password))
                else:
                    print("Sorry, email and password information could not be updated")

            elif choice=="4":
                print("Returning...")
                time.sleep(2)
                print("Returned to the previous page")
            
        else:
            print("Information update failed")

                    
    elif choice=="4":
        mail=input("Email address: ")
        password=input("Password: ")
        result=show_users_information(mail,password)

        if result:
            print(delete_account(mail,password))
        else:
            print("No account found to delete")

    elif choice=="5":
        mail=input("Email address: ")
        password=input("Password: ")
        result=show_users_information(mail,password)

        print(result)


    elif choice=="6":
        print("Exiting the program...")
        time.sleep(2)
        print("Program exited.")
        break


    else:
        print("Please try again")




        
   


        



            


        
        




        



