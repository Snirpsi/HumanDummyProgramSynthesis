#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers and enumerates words. """    
    
    import sys
    
    numbers = []
    words = []
    
    for arg in sys.argv[1:]:
        numbers.append(int(arg))
        words.append(arg)
    
    numbers.sort()
    
    for number in numbers:
        word = ''
        for word in words:
            if number % 10 == 0 and word != '':
                word = word + ' '
            word = word + str(number)
        print(word)
    
