#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and iterates over a list of words. """    
    
    ports = range(1,65535)
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    while(True):
        for port in ports:
            word = ''.join(words[port])
            print(word)
            
        time.sleep(1)
        
