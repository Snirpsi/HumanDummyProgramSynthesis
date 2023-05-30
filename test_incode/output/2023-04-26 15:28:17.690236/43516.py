#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or calculates numbers. """    
    while True:
        number = int(input("Enter a number: "))
        if number == 0: 
            break
        elif number > 0: 
            word = input("Enter a word: ")
            print(word, "is", number, "