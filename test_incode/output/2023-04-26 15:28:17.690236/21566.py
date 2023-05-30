#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a list of words or opens a list of numbers. """    
    while True:
        answer = input('Enter a word/number: ')
        if answer == 'quit':
            break
        elif answer == 'quit\n':
            break
        else:
            print(answer)
            
