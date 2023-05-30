#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports or iterates over words. """    
    
    # iterate over all ports
    for port in ports:
        
        # iterate over all words
        for word in words:
            
            # convert all ports to words
            words[word] = ports[port]
            
            # print all ports and words
            print(ports[port], word)
            
            # print all ports and words with spaces
            print(ports[port], word, sep='