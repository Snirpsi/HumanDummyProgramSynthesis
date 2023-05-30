#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words or stores a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    words = []
    
    for i in range(0, 256):
        words.append(chr(i))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
    
    words.append(chr(0xFF))
