#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            print("\nEnding program.")
            break
        else:
            print("\nConverting port %d to ASCII." % port)
            ascii_port = int(chr(port), 16)
            print("\nASCII port %d = %s" % (ascii_port, ascii_port.upper()))
