# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def encode(file):
    symbol = ''
    temp = ''
    count = 1
    with open(file, 'r', encoding="utf-8") as decode:
        for i in decode:
            temp += i
    with open('RLE_encode.txt', 'w', encoding="utf-8") as encode:
        for i in temp:
            if i != symbol:
                if symbol:
                    encode.write(str(count) + symbol)
                symbol = i
                count = 1
            else:
                count += 1
        encode.write(str(count) + symbol)


def decode(file):
    count = ''
    temp = ''
    with open(file, 'r', encoding="utf-8") as encode:
        for i in encode:
            temp += i
    with open('RLE_decode.txt', 'w', encoding="utf-8") as decode:
        for i in temp:
            if i.isdigit():
                count += i
            else:
                decode.write(i * int(count))
                count = ''

var = input('Выберите что нужно сделать:\n1 - Сжать\n2 - Восстановить:\n')
if var == '1':
    encode('RLE_encode.txt')
if var == '2':
    decode('RLE_decode.txt')


