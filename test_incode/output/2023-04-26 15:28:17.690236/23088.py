#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers. """    
    numbers = []
    while True:
        number = int(input("Enter a number: "))
        if number not in numbers:
            numbers.append(number)
        else:
            print("Number already in list")
            break
    print("The numbers are:")
    for number in numbers:
        print(number)
    
