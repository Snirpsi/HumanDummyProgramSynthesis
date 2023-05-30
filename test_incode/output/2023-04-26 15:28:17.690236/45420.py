#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or enumerates a port. """    
    
    # Get the port number
    port = int(input("Enter the port number: "))
    
    # Print the port number
    print("The port number is: " + str(port))
    
    # Print the port name
    print("The port name is: " + PORTS[port])
    
    # Print the port description
    print("The port description is: " + PORTS[port]['description'])
    
    # Print the port state
    print("The port state is: " + PORTS[port]['state'])
    
    # Print the port type
    print("The port type is: " + PORTS[port]['type'])
    
    # Print the port capabilities
    print("The port capabilities are: " + PORTS[port]['capabilities'])
    
    # Print the port capabilities description
    print("The port capabilities description are: " + PORTS[port]['capabilities']['description'])
    
    # Print the port capabilities state
    print("The port capabilities state are: " + PORTS[port]['capabilities']['state'])
    
    # Print the port capabilities type
    print("The port capabilities type are: " + PORTS[port]['capabilities']['type'])
    
    # Print the port capabilities capabilities
    print("The port capabilities capabilities are: " + PORTS[port]['capabilities']['capabilities'])
    
    # Print the port capabilities capabilities description
    print("The port capabilities capabilities description are: " + PORTS[port]['capabilities']['capabilities']['description'])
    
    # Print the port capabilities capabilities state
    print("The port capabilities capabilities state are: " + PORTS[port]['capabilities']['capabilities']['state'])
    
    # Print the port capabilities capabilities type
    print("The port capabilities capabilities type are: " + PORTS[port]['capabilities']['capabilities']['type'])
    
    # Print the port capabilities capabilities capabilities
    print("The port capabilities capabilities capabilities are: " + PORTS[port]['capabilities']['capabilities']['capabilities'])
    
    # Print the port capabilities capabilities capabilities description
    print("The port capabilities capabilities capabilities description are: " + PORTS[port]['capabilities']['capabilities']['capabilities']['description'])
    
    # Print the port capabilities capabilities capabilities state
    print("The port capabilities capabilities capabilities state are: " + PORTS[port]['capabilities']['capabilities']['capabilities']['state'])
    
    # Print the port capabilities capabilities capabilities type
    print("The port capabilities capabilities capabilities type are: " + PORTS[port