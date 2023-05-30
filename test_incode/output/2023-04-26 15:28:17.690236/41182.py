#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers. """    
    
    while True:
        number = input("Enter a number: ")
        
        if number == 'done':
            break
        
        try:
            number = int(number)
        except ValueError:
            print("That is not a number. Try again.")
            continue
        
        if number > 0:
            print(number)
        else:
            print("That number is negative. Try again.")
            continue
        
        print("Goodbye.")
        
