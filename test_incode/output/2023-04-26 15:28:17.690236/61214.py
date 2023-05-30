#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    if number == "*":
        print("Multiplying %d with %d" % (number, number))
        
        for i in range(int(number)):
            print(number * i)
    else:
        print("Enumerating %d" % number)
        for i in range(int(number)):
            print(i)
        
    print("Done.")
    
