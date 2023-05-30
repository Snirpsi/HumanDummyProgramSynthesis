#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        numbers.append(int(number))
        
        if number == 'q':
            break
            
    print("The list of numbers is {}".format(numbers))
    
