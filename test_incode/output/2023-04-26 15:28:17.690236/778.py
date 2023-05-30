#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and enumerates a list of numbers. """    
    ports = [int(p) for p in sys.argv[1:]]
    ports.remove(ports[0])
    ports.sort()
    
    ports_str = ""
    for p in ports:
        ports_str += str(p) + ", "
    ports_str = ports_str[:-2]
    
    ports_str = ports_str[:-1]
    
    print("Ports currently in use: " + ports_str)
    
    while True:
        try:
            port = int(input("Enter a port to remove: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        
        if port in ports:
            ports.remove(port)
            ports.sort()
            
            ports_str = ""
            for p in ports:
                ports_str += str(p) + ", "
            ports_str = ports_str[:-2]
            
            ports_str = ports_str[:-1]
            
            print("Ports currently in use: " + ports_str)
        else:
            print("Port " + str(port) + " is not in use.")
            
        
