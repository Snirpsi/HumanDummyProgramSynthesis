#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words and returns a list of numbers. """    
    
    words = removeWords(sys.argv[1])
    
    numbers = []
    for word in words:
        numbers.append(int(word))
    
    print(numbers)
    
