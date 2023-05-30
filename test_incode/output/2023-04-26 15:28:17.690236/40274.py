#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or removes all ports. """    
    while True:
        port = input("Enter a port number: ")
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        if port == -1:
            break
        
        # Remove all ports
        remove_all_ports(port)
        
        # Convert port
        convert_port(port)
        
        # Print results
        print("Port {} converted".format(port))
        
        # Wait for input
        input("Press Enter to continue...")
        
        # Exit loop
        break
        
