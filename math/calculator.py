from calculator1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    print(f"{a:d} + {b:d} = {add(a, b)}")
    print(f"{a:d} + {b:d} = {sub(a, b)}")
    print(f"{a:d} + {b:d} = {mul(a, b)}")
    print(f"{a:d} + {b:d} = {div(a, b)}")