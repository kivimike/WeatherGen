import random
from datetime import datetime, timedelta

areas = [x for x in range(20)]

def create_log_event(dt, area):
    time = dt.strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
    temp = f'{time},area{area},sensor{random.randint(1, 1000)}_temp, {random.randint(-20, 50)}\n'
    pres = f'{time},area{area},sensor{random.randint(1, 1000)}_pres, {random.randint(728, 812)}\n'
    hum = f'{time},area{area},sensor{random.randint(1, 1000)}_hum, {random.randint(0, 100)}\n'
    return temp, pres, hum

def create_data(filename):
    dt = datetime.now()
    with open(filename, 'a') as f:
        for i in range(30):
            for area in areas:
                log = create_log_event(dt, area)
                f.writelines(log[0])
                f.writelines(log[1])
                f.writelines(log[2])
                dt += timedelta(minutes=random.randint(0, 1), seconds=random.randint(0, 60),
                                milliseconds=random.randint(0, 10000))
            dt += timedelta(minutes=random.randint(2, 10), seconds=random.randint(0, 60), milliseconds=random.randint(0,10000))


create_data('hello')