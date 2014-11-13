import argparse

def fib(iterations):
    a = 1
    print("Fibboncci number 1 is {}.".format(a))
    b = 1
    print("Fibboncci number 2 is {}.".format(b))
    for i in range(3,iterations+1):
        c = a + b
        a = b
        b = c
        print("Fibboncci number {} is {}.".format(i, b))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("iterations", help="Number of iterations to run.", type=int)
    args = parser.parse_args()
    fib(args.iterations)