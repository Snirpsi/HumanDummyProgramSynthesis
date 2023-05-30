#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    wordlist = ['apple', 'banana', 'cherry']
    
    while True:
        wordlist = list(filter(lambda x: x != '', wordlist))
        
        print(wordlist)
        
        time.sleep(1)
        
