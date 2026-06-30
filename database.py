import sqlite3 as sql


connect=sql.connect("Accounts_Information.db")
cursor=connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS mail_accounts(id INTEGER PRIMARY KEY, mail_Address TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
connect.commit()
connect.close()

def add_account(account_mail,account_password):
    try:
        connect=sql.connect("Accounts_Information.db")
        cursor=connect.cursor()
        cursor.execute("INSERT INTO mail_accounts (mail_Address,password) VALUES(?,?)",(account_mail,account_password))
        connect.commit()
        connect.close()
    except sql.IntegrityError as e:
        return f"error: {e}" 
    except Exception as e:
        return f"error: {e}"
    return "added "

def update_account(account_mail,account_password,new_account_mail=None,new_account_password=None):
    try:
        connect=sql.connect("Accounts_Information.db")
        cursor=connect.cursor()

        if new_account_mail and new_account_password:
            cursor.execute("UPDATE mail_accounts SET mail_Address=? , password=? WHERE mail_Address=? AND password=?",(new_account_mail,new_account_password,account_mail,account_password))
            connect.commit()
            return "Email and password have been updated"
            
        elif new_account_password:
            cursor.execute("UPDATE mail_accounts SET password=? WHERE mail_Address=? AND password=?",(new_account_password,account_mail,account_password))
            connect.commit()
            return "Password updated"
            
        elif new_account_mail:
            cursor.execute("UPDATE mail_accounts SET mail_Address=? WHERE mail_Address=? AND password=?",(new_account_mail,account_mail,account_password))
            connect.commit()
            return "Email address updated"
        
        return "No changes have been made"

    except sql.IntegrityError as e:
        return f"{e}"
    
    finally:
        connect.close()

def delete_account(account_mail,account_password):
    try:
        connect=sql.connect("Accounts_Information.db")
        cursor=connect.cursor()

        cursor.execute("DELETE FROM mail_accounts WHERE mail_Address=? AND password=?",(account_mail,account_password))
        connect.commit()
        connect.close()

        if cursor.rowcount > 0:
            return "Account deleted"
        else:
            return "No account found to delete"

    except Exception as e:
        print(f"error: {e}")
        return None
    

def show_users_information(mail,password):

    try:
        connect=sql.connect("Accounts_Information.db")
        cursor=connect.cursor()

        cursor.execute("SELECT * FROM mail_accounts WHERE mail_Address=? AND password=?",(mail,password))
        find_Accounts=cursor.fetchone()
        connect.close()

        if find_Accounts is None:
           return f"Email address: {mail} and password: {password} were not found"
           
        else:
           return f"Email address : {find_Accounts[1]} , password : {find_Accounts[2]} were found "

    except Exception as e:
        return f"error:{e}"
        
    
    
    

    


    

