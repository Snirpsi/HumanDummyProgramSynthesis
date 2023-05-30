#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or iterates over a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0:
            words = []
            
            for i in range(number):
                words.append(sys.argv[2])
                
            print(" ".join(words))
        else:
            print(" ".join(sys.argv[2:]))
    else:
        print(" ".join(sys.argv[2:]))
    
