from accounts import user_temp as acc


def create_acc():
    with open(r'accounts\user.txt', 'a') as file:
        for i in acc.user:
            user_inp = input(f'Enter your {i.lower()}')
            file.write(f"{i}: {user_inp}\n")
            
            

            
         
    