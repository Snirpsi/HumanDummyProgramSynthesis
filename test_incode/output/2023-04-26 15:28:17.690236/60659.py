#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and multiplyes numbers. """    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        
        answer = number * number
        
        print("The answer is {}".format(answer))
        
        if number == 