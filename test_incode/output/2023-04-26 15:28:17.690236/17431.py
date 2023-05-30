#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports or opens a port. """    
    
    ports = []
    
    # Open a port if none is given
    if len(sys.argv) == 1:
        ports.append(8080)
    
    # Open a port if given as an argument
    elif len(sys.argv) == 2:
        ports.append(int(sys.argv[1]))
    
    # Open a port if given as a list of ports
    elif len(sys.argv) == 3:
        ports.extend(sys.argv[1:])
    
    # Open a port if given as a list of ports and a name
    elif len(sys.argv) == 4:
        ports.extend(sys.argv[1:])
        
    # Open a port if given as a list of ports and a name and port
    elif len(sys.argv) == 5:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
    
    # Open a port if given as a list of ports and a name and port and name
    elif len(sys.argv) == 6:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
    
    # Open a port if given as a list of ports and a name and port and name and port
    elif len(sys.argv) == 7:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
        ports.append(sys.argv[4])
    
    # Open a port if given as a list of ports and a name and port and name and port
    elif len(sys.argv) == 8:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
        ports.append(sys.argv[4])
        ports.append(sys.argv[5])
    
    # Open a port if given as a list of ports and a name and port and name and port
    elif len(sys.argv) == 9:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
        ports.append(sys.argv[4])
        ports.append(sys.argv[5])
        ports.append(sys.argv[6])
    
    # Open a port if given as a list of ports and a name and port and name and port
    elif len(sys.argv) == 10:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
        ports.append(sys.argv[4])
        ports.append(sys.argv[5])
        ports.append(sys.argv[6])
        ports.append(sys.argv[7])
    
    # Open a port if given as a list of ports and a name and port and name and port
    elif len(sys.argv) == 11:
        ports.extend(sys.argv[1:])
        ports.append(int(sys.argv[2]))
        ports.append(sys.argv[3])
        ports.append(sys.argv[4])
        ports.append(sys.argv[5])
        ports.append(sys.argv[6])
        ports.append(sys.argv[7])
        ports.append(sys.argv[8])
    
    # Open 