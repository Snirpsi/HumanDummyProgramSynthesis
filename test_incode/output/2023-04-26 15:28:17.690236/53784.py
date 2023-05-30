#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits and iterates over a port. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    port = 5000
    
    # Create a socket and bind the port to it.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', port))
    
    # Create a TCP socket and connect to the port on the server.
    s.settimeout(10)
    s.connect((host, port))
    
    # Send the fruits over the socket and print the results.
    for fruit in fruits:
        s.send(fruit + '\n')
        print('Sent ' + fruit)
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
    # Close the socket and quit.
    s.close()
    
    # Print the results of the connection.
    print('Connection closed.')
    
