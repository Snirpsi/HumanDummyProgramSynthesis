#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words and enumerates all ports. """    
    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    ports = ['port1', 'port2', 'port3', 'port4', 'port5']
    
    for index, word in enumerate(words):
        for port in ports:
            print('{} - {}'.format(word, port))
