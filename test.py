# def quadr(x):
#     return x**2


# list = [(i, quadr(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)


def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8  15 23 38'.split()
res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x**2), res)
print(res)