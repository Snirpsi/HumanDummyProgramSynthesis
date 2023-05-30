#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or multiplyes a port. """    
    port = int(sys.argv[1])
    
    if port == 0 or port == 9999:
        print("Invalid port number")
        sys.exit()
    
    ports = [port]
    
    if len(sys.argv) > 2:
        ports = sys.argv[2:]
    
    for port in ports:
        
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            sys.exit()
    
        if port == 0 or port == 9999:
            print("Invalid port number")
            sys.exit()
    
        if port in ports:
            ports.remove(port)
    
    if len(ports) == 0:
        print("No ports found")
        sys.exit()
    
    if len(ports) == 1:
        port = ports[0]
    
    print("Ports found: ", ports)
    
    ports_str = ""
    for port in ports:
        ports_str += str(port) + " "
    
    print("Ports string: ", ports_str)
    
    ports_str = ports_str.strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    
    if len(ports_str) == 1:
        ports_str = ports_str[0]
    
    ports_str = ports_str[0].strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    
    if len(ports_str) == 1:
        ports_str = ports_str[0]
    
    ports_str = ports_str[0].strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    
    if len(ports_str) == 1:
        ports_str = ports_str[0]
    
    ports_str = ports_str[0].strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    
    if len(ports_str) == 1:
        ports_str = ports_str[0]
    
    ports_str = ports_str[0].strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    
    if len(ports_str) == 1:
        ports_str = ports_str[0]
    
    ports_str = ports_str[0].strip()
    
    if len(ports_str) == 0:
        print("No ports found")
        sys.exit()
    
    ports_str = ports_str.split(" ")
    