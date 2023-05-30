#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers and multiplyes a list of words. """    
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    words = ['word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word', 'word']
    
    for number in numbers:
        for word in words:
            print(number * word)
    
