#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port or calculates a list of words. """    
    
    port = 0
    
    while True:
        port = port + 1
        
        if port == len(sys.argv):
            break
        
        word = sys.argv[1]
        
        if word == 'stop':
            break
        
        if word == 'help':
            print('''
            Usage: python3 wordlist.py [word]
            
            wordlist.py stop
            
            wordlist.py help
            
            wordlist.py [word] [word]
            
            wordlist.py [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
            wordlist.py [word] [word] [word] [word] [word] [word] [word]
            
