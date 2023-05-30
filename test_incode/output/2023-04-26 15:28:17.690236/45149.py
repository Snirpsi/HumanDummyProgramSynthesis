#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and calculates a list of numbers. """    
    port = 5000
    numbers = []
    
    # Open the port and read it in
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Read in one byte at a time
    while True:
        byte = sock.recv(1)
        
        # If the byte is equal to '\n', then break out of the loop
        if byte == '\n':
            break
        
        # If the byte is equal to '-', then add it to the list
        if byte == '-':
            numbers.append(int(byte))
            
    # Close the socket
    sock.close()
    
    # Print out the list of numbers
    print(numbers)
    
    # Close the port
    sock.close()
    
    # Close the program
    exit(0)
    
# Run the program
if __name__ == '__main__':
    main()
    
# 