#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers and returns a list of words. """    
    numbers = [int(i) for i in input("Enter a number: ").split()]
    words = []
    while numbers:
        words.append(" ".join(str(x) for x in numbers))
        numbers = [int(i) for i in input("Enter a number: ").split()]
    print(words)
