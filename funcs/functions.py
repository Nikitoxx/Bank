from accounts import user_temp as acc
import os


def check_phone_num(number):
    template = '+373xxxxxxxx'
    for i in range(len(template)):
        if len(template) != len(number):
            return False
        elif number[i] == template[i]:
            continue
        elif template[i] == 'x' and number[i].isdigit():
            continue
        else:
            return False
    else:
        return True
     

def create_acc(user):
    with open(f'accounts\\{user}.txt', 'a') as file:
        for i in acc.user:
            if i.lower() == 'phone number':
                while True:
                    user_inp = input(f'Enter your {i.lower()}: ')
                    if check_phone_num(user_inp):
                        file.write(f"{i}: {user_inp}\n")
                        break
                    else:
                        print('Wrong phone number format! Try again!')
                        continue
            else:
                user_inp = input(f'Enter your {i.lower()}: ')
                file.write(f"{i}: {user_inp}\n")
            
            
def chk_acc_exist(login):
    return  True if os.path.isfile(f'accounts\\{login}.txt') else False









    
            
            

            
         
    