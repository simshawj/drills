def fib(iterations):
    a = 1
    print("Fibboncci number 1 is {}.".format(a))
    b = 1
    print("Fibboncci number 2 is {}.".format(b))
    for(i = 3; i < iterations; i++):
        c = a + b
        a = b
        b = c
        print("Fibboncci number {} is {}.".format(i, b))