#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers and opens a list of words. """    
    
    while True:
        number = input("Enter a number: ")
        
        if number == "quit":
            break
        
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if number < 0 or number > 1000:
            print("Invalid input. Try again.")
            continue
        
        if number % 2 == 0:
            print("{} is a perfect square".format(number))
        else:
            print("{} is not a perfect square".format(number))
        
        print("\n")
        
