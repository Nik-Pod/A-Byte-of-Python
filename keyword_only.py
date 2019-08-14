def func(initial = 5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)
func(19, 3, 15, extra_number = 11)
