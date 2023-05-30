#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input and removes all ports. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        
        port = str(port)
        
        # Remove port from list
        ports.remove(port)
        
        # Print port to screen
        print("Port removed: " + port)
        
        # Calculate remaining ports
        remaining_ports = ports - set(ports)
        
        # Print remaining ports
        print("Remaining ports: " + str(remaining_ports))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage = remaining_ports / float(len(ports))
        
        # Print remaining ports percentage
        print("Remaining ports percentage: " + str(remaining_ports_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage = remaining_ports_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage: " + str(remaining_ports_percentage_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage_percentage = remaining_ports_percentage_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage percentage: " + str(remaining_ports_percentage_percentage_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage_percentage_percentage = remaining_ports_percentage_percentage_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage percentage percentage: " + str(remaining_ports_percentage_percentage_percentage_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage_percentage_percentage_percentage = remaining_ports_percentage_percentage_percentage_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage percentage percentage: " + str(remaining_ports_percentage_percentage_percentage_percentage_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage_percentage_percentage_percentage = remaining_ports_percentage_percentage_percentage_percentage_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage percentage percentage percentage: " + str(remaining_ports_percentage_percentage_percentage_percentage_percentage))
        
        # Calculate remaining ports percentage
        remaining_ports_percentage_percentage_percentage_percentage_percentage_percentage = remaining_ports_percentage_percentage_percentage_percentage_percentage * 100
        
        # Print remaining ports percentage
        print("Remaining ports percentage percentage percentage percentage percentage: " + str(remaining_