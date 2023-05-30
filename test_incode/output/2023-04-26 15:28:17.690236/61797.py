#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and calculates words. """    
    numbers = input("Enter a number: ")
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers = [x * 2 for x in numbers]
    numbers = [str(x) for x in numbers]
    numbers = " ".join(numbers)
    print(numbers)

<|/ file ext=.py source=github |>