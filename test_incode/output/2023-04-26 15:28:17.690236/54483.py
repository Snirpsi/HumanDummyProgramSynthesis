#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or removes words. """    
    
    ports = input("Enter ports: ").split()
    
    if len(ports) == 0:
        print("No ports given.")
    else:
        for port in ports:
            if port not in ports:
                print("Port {} is not in the list".format(port))
            else:
                ports.remove(port)
    
    print("Ports removed: {}".format(ports))
    
    
