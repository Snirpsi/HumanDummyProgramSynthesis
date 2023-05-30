#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports. """    
    ports = []
    
    # Iterate through all available ports
    for port in range(0, 65535):
        # Check if port is available
        if port in os.listdir("/dev/"):
            ports.append(port)
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -X")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -X")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -X")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -X")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -X")
    
    # Print all ports
    for port in ports:
        print(port)
    
    # Close all ports
    for port in ports:
        os.system("sudo iptables -F")
    
    # Print all ports
    for port in ports:
        print(port)
    
