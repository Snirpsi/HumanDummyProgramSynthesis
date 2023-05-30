#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints words and multiplyes a list of numbers. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    numbers = [1, 2, 3, 4, 5, 6]
    
    for word in words:
        for number in numbers:
            print(word * number)
        
