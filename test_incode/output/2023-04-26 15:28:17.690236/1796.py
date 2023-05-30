#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and adds fruits. """    
    
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    sock.bind(('', 80))
    
    # Listen for incoming connections
    sock.listen(1)
    
    # Accept a connection
    conn, addr = sock.accept()
    
    # Receive the fruit from the client
    fruit = conn.recv(1024)
    
    # Send the fruit to the client
    conn.sendall(fruit)
    
    # Close the connection
    conn.close()
    
    # Close the socket
    sock.close()
    
