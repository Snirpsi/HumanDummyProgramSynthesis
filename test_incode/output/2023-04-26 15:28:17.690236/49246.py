#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and enumerates numbers. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.append(line)
    
    numbers = map(int, numbers)
    
    words = sorted(words)
    numbers = sorted(numbers)
    
    for index, word in enumerate(words):
        print('{0}: {1}'.format(word, numbers[index]))
    
