#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and converts a list of numbers. """    
    import sys
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    numbers = []
    for arg in sys.argv[2:]:
        numbers.append(int(arg))
    
    words.sort()
    numbers.sort()
    
    for word in words:
        print(word)
        for number in numbers:
            print(number)
    
