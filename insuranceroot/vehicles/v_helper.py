from random import randint
import datetime


def gen_policy_number():
    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    time_now = str(today.hour) + str(today.minute) + str(today.second)

    return 'POL/INS/'+year+month+day+"/"+time_now+"/"+str(randint(1256713, 9245658))
