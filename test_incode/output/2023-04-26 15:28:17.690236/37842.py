#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words and opens a port. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    port = "/dev/ttyUSB0"
    
    port = open("/dev/ttyUSB0", "w")
    
    port.write(word)
    port.close()
    
    print("Opened port %s" % port)
    
    
