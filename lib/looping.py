#!/usr/bin/env python3

def happy_new_year():
    """Prints a countdown from 10 to 1, then prints 'Happy New Year!'."""
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")


def square_integers(int_list):
    """Returns a list of squared integers."""
    return [x ** 2 for x in int_list]


def fizzbuzz():
    """Prints numbers from 1 to 100 with specific rules for multiples of 3 and 5."""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
