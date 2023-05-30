#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and calculates numbers. """    
    while True:
        number = input("Enter a number: ")
        number = int(number)
        print(number)
        
        if number == -1:
            break
        
        answer = number + number
        print(answer)
        
        if answer == -1:
            break
        
        print("The answer is {}".format(answer))
        
        print("Press Enter to continue...")
        
