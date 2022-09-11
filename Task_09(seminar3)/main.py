# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды)
#  - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time


def random(min, max):
    num = time.time_ns()
    num = str(num)
    num = num[11:17]
    num = int(num)
    while num > max:
        num -= (max - min) - 1
    return num


print(random(1, 1000))
