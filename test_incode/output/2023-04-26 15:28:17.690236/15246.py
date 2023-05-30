#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and iterates over a list of numbers. """    
    
    numbers = range(1,10)
    
    while True:
        number = input("Enter a number: ")
        if number == 'q':
            break
        
        numbers.append(int(number))
    
    print("The numbers are:")
    for number in numbers:
        print(number)
    
    print("The numbers are:")
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 3 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 5 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 7 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 11 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 13 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 17 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 19 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 23 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 29 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 31 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 37 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 41 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 47 == 0:
            print(number)
        else:
            print("Not a prime")
    
    print("The numbers are:")
    for number in numbers:
        if number % 53 == 0:
            print(number)