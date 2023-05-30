#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports and returns a list of words. """    
    ports = convert_ports()
    words = convert_words()
    
    for port in ports:
        for word in words:
            if port == word:
                print "%s %s" % (port, word)
    
