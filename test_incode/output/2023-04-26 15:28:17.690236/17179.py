#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    words.sort()
    
    for word in words:
        print(word)
    
    print("\nDone")
    
