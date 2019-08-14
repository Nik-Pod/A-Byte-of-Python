while True:
    s = input('Введите строку: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Строка слишком маленькая')
        continue
    print('В строке {0} символов'.format(len(s)))
print('Завершение')