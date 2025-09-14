import os


def check_phoneNum(number):
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


def check_ID(idnum):
    template = 'B2006xxxxxxxx'
    for i in range(len(template)):
        if len(template) != len(idnum):
            return False
        elif idnum[i] == template[i]:
            continue
        elif template[i] == 'x' and idnum[i].isdigit():
            continue
        else:
            return False
    else:
        return True


def chk_acc_exist(login):
    return  True if os.path.isfile(f'accounts\\{login}.txt') else False
