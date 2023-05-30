#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or adds a list of words. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        else:
            print(number)
            
            for word in words:
                print(word, 'is', number % 