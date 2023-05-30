#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port. """    
    port = int(sys.argv[1])
    
    # Store the port in a file
    file = open('ports.txt', 'w')
    file.write(str(port))
    file.close()
    
    # Print the port in a file
    file = open('ports.txt', 'r')
    port = file.read()
    file.close()
    
    # Print the port in a terminal
    print(port)
    
    # Close the file
    file.close()
    
    # Close the terminal
    