#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or multiplyes a port. """    
    port = int(sys.argv[1])
    
    if port < 1 or port > 65535:
        print("Invalid port")
        sys.exit()
    
    ports = [port]
    
    while True:
        ports.append(int(input("Enter a port number [1-65535]: ")))
        
        if ports[-1] > 65535:
            print("Port number too large")
            sys.exit()
        
        if ports[-1] == 1:
            ports.pop()
            
        if ports[-1] == port:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0]:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 1:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 2:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 3:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 4:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 5:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 6:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 7:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 8:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 9:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 10:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 11:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 12:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 13:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 14:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 15:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 16:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 17:
            print("Port number already in use")
            sys.exit()
        
        if ports[-1] == ports[0] + 18: