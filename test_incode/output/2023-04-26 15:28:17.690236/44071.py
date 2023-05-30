#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words and iterates over all ports. """    
    
    words = ['word1', 'word2', 'word3']
    
    for port in range(1, 10):
        print('Port {}: {}'.format(port, words[port-1]))
        
