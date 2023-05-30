#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or adds words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <number|word>" % sys.argv[0])
        sys.exit(1)
    
    number = sys.argv[1]
    
    if number.isdigit():
        number = int(number)
        
        if number > 0:
            print(str(number))
        else:
            print("0")
    else:
        words = number.split()
        
        for word in words:
            print(word)
            
