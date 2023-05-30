#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and stores words. """    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
        else:
            break
    
    words.sort()
    for word in words:
        print(word)
    
