#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or multiplyes a list of words. """    
    
    ports = range(65535)
    
    words = ["word1", "word2", "word3"]
    
    for port in ports:
        for word in words:
            print("Port {} 