#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or returns a list of words. """    
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else None
    
    if port is not None:
        port = port + 1
        
    words = []
    
    for word in open('words.txt').read().split():
        words.append(word)
    
    if port is not None:
        words = [word for word in words if word[0] == str(port)]
    
    print(word