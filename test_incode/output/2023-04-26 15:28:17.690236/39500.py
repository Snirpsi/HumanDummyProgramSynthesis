#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of numbers and adds words. """    
    numbers = [1,2,3,4,5]
    words = ['one','two','three','four','five']
    
    for number in numbers:
        for word in words:
            print(word+number)
    
