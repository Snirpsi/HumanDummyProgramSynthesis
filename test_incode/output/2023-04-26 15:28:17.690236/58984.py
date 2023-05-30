#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input and stores a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        numbers.append(int(number))
        print("Numbers stored.")
        
        if number == 'q':
            break
        
