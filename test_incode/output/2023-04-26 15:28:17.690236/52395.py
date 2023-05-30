#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or removes all ports. """    
    import sys
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        for word in words:
            print(word)
    else:
        print('Usage: python remove_ports.py word1 word2 word3')
        
    
