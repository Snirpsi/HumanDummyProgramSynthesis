#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or prints all ports. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python listports.py [port]")
        sys.exit()
    
    port = int(sys.argv[1])
    
    portlist = list()
    
    for i in range(1,65535):
        portlist.append(i)
    
    portlist.sort()
    
    print("Ports open:")
    
    for port in portlist:
        print("  " + str(port))
    
    print("\nTo close a port, type 'quit' followed by a number.")
    
    port = int(input("Enter a port number: "))
    
    if port in portlist:
        portlist.remove(port)
    
    portlist.sort()
    
    print("Ports closed:")
    
    for port in portlist:
        print("  " + str(port))
    
    print("\nTo quit this program, type 'quit'.")
    
    port = int(input("Enter a port number: "))
    
    if port in portlist:
        portlist.remove(port)
    
    portlist.sort()
    
    print("Ports quit:")
    
    for port in portlist:
        print("  " + str(port))
    
    print("\nTo exit, type 'quit'.")
    
    port = int(input("Enter a port number: "))
    
    if port in portlist:
        portlist.remove(port)
    
    portlist.sort()
    
    print("Ports quit:")
    
    for port in portlist:
        print("  " + str(port))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
