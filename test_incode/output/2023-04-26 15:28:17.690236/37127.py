#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits and returns numbers. """    
    fruits = ['apple', 'banana', 'orange', 'mango', 'cherry', 'grape']
    numbers = []
    for fruit in fruits:
        if fruit not in numbers:
            numbers.append(fruit)
    return numbers

<|/ file filename=fruits.py source=github |>