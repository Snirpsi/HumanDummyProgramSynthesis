#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or prints words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port < 0 or port > 65535:
            print("Port must be between 0 and 65535.")
            sys.exit()
        
        print("\nWords:")
        
        for i in range(port):
            print(chr(ord('a') + i))
    else:
        print("Usage: python3 words.py")
        
