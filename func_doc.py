def printMax(a, b):
    '''Выводит максимальное из двух чисел

    Оба значения должны быть целыми числами'''
    if a > b:
        print(a, 'наибольшее')
    elif b > a:
        print(b, 'наибольшее')
    else:
        print('Числа равны')
printMax(2, 8)
print(printMax.__doc__)
