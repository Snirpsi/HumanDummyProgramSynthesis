#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts user input or multiplyes a list of words. """    
    
    words = input("Enter a word: ")
    
    if words == "":
        print("You didn't enter a word.")
    else:
        words = words.split()
        
        words = [int(x) for x in words]
        
        words = [x*