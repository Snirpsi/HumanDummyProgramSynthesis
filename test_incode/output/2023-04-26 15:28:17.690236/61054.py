#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words or returns a port. """    
    import sys
    if len(sys.argv) > 1:
        word = sys.argv[1]
        port = int(sys.argv[2])
        
        if word in ports:
            ports.remove(word)
        else:
            print("Port %s does not exist" % word)
    else:
        print("Usage: %s <word> <port>" % sys.argv[0])
        
