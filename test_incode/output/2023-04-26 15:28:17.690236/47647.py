#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or multiplyes a port. """    
    words = ['cat', 'dog', 'mouse']
    ports = [80, 443]
    
    for word in words:
        for port in ports:
            print(word + ' is on port ' + str(port))
    
