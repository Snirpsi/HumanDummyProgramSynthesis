#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a list of words and prints numbers. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse', 'pig', 'cow', 'horse', 'sheep']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    for word in words:
        print(word)
        for number in numbers:
            print(number, end=' ')
        print()
    
