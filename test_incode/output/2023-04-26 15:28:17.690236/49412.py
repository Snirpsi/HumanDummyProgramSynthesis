#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and converts a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    words = words[:]
    
    words.pop(port)
    
    words = [word.upper() for word in words]
    
    words = [word for word in words if word not in ['