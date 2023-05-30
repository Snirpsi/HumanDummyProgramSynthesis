#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers. """    
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            print(int(num))
        else:
            print("Invalid input. Try again.")
            
        
