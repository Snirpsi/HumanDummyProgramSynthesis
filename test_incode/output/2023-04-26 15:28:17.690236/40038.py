#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words. """    
    while True:
        words = open('words.txt').read().splitlines()
        for word in words:
            print(word)
        time.sleep(1)
        
