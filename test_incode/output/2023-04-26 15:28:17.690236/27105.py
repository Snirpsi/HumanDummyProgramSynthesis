#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for arg in sys.argv[1:]:
            words.append(arg)
        
        for word in words:
            print(word*2)
    else:
        print("Usage: python server.py <words>")
    
