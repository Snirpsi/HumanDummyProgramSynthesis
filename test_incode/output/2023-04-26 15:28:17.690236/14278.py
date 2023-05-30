#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and returns words. """    
    
    while True:
        number = int(input("Enter a number: "))
        
        if number < 10:
            print("The number is too small.")
        elif number > 1000:
            print("The number is too large.")
        else:
            print("The number is {}.".format(number))
        
        word = input("Enter a word: ")
        
        if word == "quit":
            print("Goodbye.")
            break
        else:
            print("The word is {}.".format(word))
            
