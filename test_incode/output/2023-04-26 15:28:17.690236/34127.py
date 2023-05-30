#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    words = [w.strip() for w in words]
    
    port = str(port)
    
    print("Port:", port)
    
    for word in words:
        print(word, "