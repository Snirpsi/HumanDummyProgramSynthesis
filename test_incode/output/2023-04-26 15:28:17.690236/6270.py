#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers and adds a port. """    
    port = int(input("Enter a port number: "))
    
    numbers = []
    
    while True:
        try:
            numbers.append(int(input("Enter a number: ")))
        except ValueError:
            print("Invalid input")
        else:
            break
    
    numbers.append(port)
    
    numbers = list(set(numbers))
    
    print("The ports available are:")
    
    for number in numbers:
        print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number == port:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number != port:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number < port:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port and number < port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number < port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number < port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number < port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number > port + 1:
            print(number)
    
    print("The ports available are:")
    
    for number in numbers:
        if number < port + 1:
            print(number)
    
    print("The ports available are:")