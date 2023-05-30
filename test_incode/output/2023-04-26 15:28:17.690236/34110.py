#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and stores a list of numbers. """    
    ports = []
    
    # Enumerate all ports
    for port in range(1, 65535):
        ports.append(port)
    
    # Print the ports
    print("Ports:")
    for port in ports:
        print(port)
    
    # Print the list of numbers
    print("Numbers:")
    for port in ports:
        print(port)
    
    # Print the list of numbers with leading zeros
    print("Numbers with leading zeros:")
    for port in ports:
        print(str(port).zfill(2))
    
    # Print the list of numbers with leading zeros
    print("Numbers with leading zeros and spaces:")
    for port in ports:
        print(str(port).zfill(2) + " ")
    
    # Print the list of numbers with leading zeros
    print("Numbers with leading zeros and spaces and dashes:")
    for port in ports:
        print(str(port).zfill(2) + " -")
    
    # Print the list of numbers with leading zeros
    print("Numbers with leading zeros and spaces and dashes and periods:")
    for port in ports:
        print(str(port).zfill(2) + " -.")
    
    # Print the list of numbers with leading zeros
    print("Numbers with leading zeros and spaces and dashes and periods and apostrophes:")
    for port in ports:
        print(str(port).zfill(2) + " -