#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and enumerates a list of words. """    
    
    ports = range(5000, 5999)
    words = []
    for port in ports:
        words.extend(enumerateWords(port))
    
    words.sort()
    
    for word in words:
        print('%d\t%s' % (word[0], word[1]))
    
