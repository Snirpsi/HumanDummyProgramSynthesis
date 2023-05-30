#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input and stores numbers. """    
    while True:
        number = int(input("Enter a number: "))
        numbers.append(number)
        
        if number == 1000:
            break
        
    print("The numbers 