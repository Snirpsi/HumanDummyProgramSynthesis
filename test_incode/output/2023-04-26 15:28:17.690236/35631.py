#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    while True:
        numbers = input("Enter numbers: ")
        numbers = numbers.split()
        for number in numbers:
            if number.isdigit():
                number = int(number)
                print(number)
            else:
                print("Invalid input")
