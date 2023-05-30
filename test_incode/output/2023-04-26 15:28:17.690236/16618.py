#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and iterates over a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <wordlist>" % sys.argv[0])
        exit(1)
    
    wordlist = sys.argv[1]
    
    words = []
    for line in open(wordlist):
        words.append(line.strip())
    
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    numbers = sorted(numbers)
    
    words = sorted(words)
    
    for number in numbers:
        for word in words:
            if number == word:
                print(word)
                break
    
