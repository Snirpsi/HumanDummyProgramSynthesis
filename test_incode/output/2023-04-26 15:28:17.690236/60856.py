#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and adds all ports. """    
    
    words = ['word1', 'word2', 'word3']
    ports = [8080, 8081, 8082]
    
    for port in ports:
        