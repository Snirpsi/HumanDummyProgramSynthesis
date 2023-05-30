#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove-numbers.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word for word in words if word.isdigit()]
    
    print("\n".join(words))
    
