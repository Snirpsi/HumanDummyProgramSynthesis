#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or returns a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0 and port < 65536:
            
            words = []
            
            for i in range(0, port):
                words.append(chr(ord('A') + i))
            
            print(words)
            
        else:
            print("Port number must be between 0 and 65536.")
            
    else:
        print("Usage: python ports.py <port>")
        
