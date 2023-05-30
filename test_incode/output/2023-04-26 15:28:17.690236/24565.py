#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports. """    
    
    # Define the ports we want to calculate
    ports = [
        Port("A", 0, 1),
        Port("B", 0, 2),
        Port("C", 0, 3),
        Port("D", 0, 4),
        Port("E", 0, 5),
        Port("F", 0, 6),
        Port("G", 0, 7),
        Port("H", 0, 8),
        Port("I", 0, 9),
        Port("J", 0, 10),
        Port("K", 0, 11),
        Port("L", 0, 12),
        Port("M", 0, 13),
        Port("N", 0, 14),
        Port("O", 0, 15),
        Port("P", 0, 16),
        Port("Q", 0, 17),
        Port("R", 0, 18),
        Port("S", 0, 19),
        Port("T", 0, 20),
        Port("U", 0, 21),
        Port("V", 0, 22),
        Port("W", 0, 23),
        Port("X", 0, 24),
        Port("Y", 0, 25),
        Port("Z", 0, 26),
    ]
    
    # Calculate the ports
    ports = calculate_ports(ports)
    
    # Print the ports
    for port in ports:
        print(port)
        
