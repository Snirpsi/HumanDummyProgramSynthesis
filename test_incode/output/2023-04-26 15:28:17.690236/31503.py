#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and adds a list of words. """    
    ports = sys.argv[1:]
    words = []
    for port in ports:
        words.extend(port.split('-'))
    
    words.sort()
    
    for word in words:
        print('%s\t%s' % (word, ports[word.index(':')]))
    
