#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of numbers and opens a port. """    
    
    # Create a socket and bind to port 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    
    # Listen for connections
    sock.listen(1)
    
    # Accept connection and print out a message
    conn, addr = sock.accept()
    
    # Send a message to the client
    conn.send('Hello World!\n')
    
    # Close the connection
    conn.close()
    
    # Close the socket
    sock.close()
    
    # Close the server
    server.