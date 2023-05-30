#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and returns a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <num1> <num2> ..." % sys.argv[0])
        sys.exit()
    
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    
    words = []
    for i in range(int(num1)):
        words.append(str(num1 * i))
    for i in range(int(num2)):
        words.append(str(num2 * i))
    
    print(" ".join(words))
    
