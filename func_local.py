x = 20
def localx(x):
    print('x равен', x)
    x = 5
    print('Замена локального x на', x)
localx(x)
print('x по прежниму', x)
