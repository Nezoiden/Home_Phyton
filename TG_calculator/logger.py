from datetime import datetime as dt
from time import time


def log(data, result):
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('logger.log', 'a', encoding='utf-8') as file:
        file.writelines(f'{time} : {data} {result}\n')
        file.write('======\n')
    


