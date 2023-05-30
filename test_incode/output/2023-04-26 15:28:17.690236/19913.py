#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or multiplyes all ports. """    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        print("Port %d: " % port)
        
        for word in range(port):
            print("%d\t" % word, end="")
        
        print("\n")
        
    print("\nDone.")
    
