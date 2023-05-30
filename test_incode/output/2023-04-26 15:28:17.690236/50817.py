#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over numbers or prints a list of words. """    
    
    words = []
    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break
        else:
            words.append(number)
    
    print(words)
    
