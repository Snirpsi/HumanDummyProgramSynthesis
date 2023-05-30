#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of numbers and removes a list of numbers. """    
    numbers = []
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        else:
            numbers.append(number)
    numbers = list(set(numbers))
    print(numbers)
    numbers.remove