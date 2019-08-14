def func():
    x = 3
    def func1():
        nonlocal x
        print('x равен', x)
        x = 10
    func1()
    print('Замена не локального x на', x)
func()
