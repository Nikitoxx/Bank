from accounts import user_temp as acc
import os


def create_acc():
    with open(r'accounts\user.txt', 'a') as file:
        for i in acc.user:
            user_inp = input(f'Enter your {i.lower()}: ')
            file.write(f"{i}: {user_inp}\n")
            
            
def chk_acc_exist(login):
    return  True if os.path.isfile(f'accounts\\{login}.txt') else False


    
            
            

            
         
    