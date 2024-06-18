import random

number = 98
print(f"{number:d} Battery street")

num = random.randint(-10, 10)
if num > 0:
    print(f"{num}Is positive")
elif num == 0:
    print(f"{num}Is zero")
else:
    print(f"{num}Is negative")

def fizzbuzz():
    """
    Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".
    """
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(f"{i:d}")
fizzbuzz()
