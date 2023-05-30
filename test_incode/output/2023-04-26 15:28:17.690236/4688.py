#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of numbers or removes words. """    
    
    import sys
    
    wordlist = sys.argv[1:]
    
    if len(wordlist) == 0:
        print('No words given.')
    else:
        wordlist = wordlist.split()
        
        print('Words:')
        for word in wordlist:
            print(word)
            
        print('Removed words:')
        for word in wordlist:
            if word not in wordlist:
                print(word)
                
        print('Done.')
    
