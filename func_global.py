x = 30
def func():
    global x
    print('x равен', x)
    x = 3
    print('Замена глобального x на', x)
func()
print('x все еще равен', x)
