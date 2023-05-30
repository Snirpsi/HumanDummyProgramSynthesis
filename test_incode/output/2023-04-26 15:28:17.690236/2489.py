#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and converts numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        
        # Convert port to binary and store in list
        binary = bin(port)
        ports.append(binary)
        
        # Print out port number
        print("Port number:", port)
        
        # Print out binary number
        print("Binary number:", binary)
        
        # Print out all port numbers
        print("All port numbers:", ports)
        
        # Print out all binary numbers
        print("All binary numbers:", binarys)
        
        # Print out all binary numbers with leading zeros
        print("All binary numbers with leading zeros:", binarys_with