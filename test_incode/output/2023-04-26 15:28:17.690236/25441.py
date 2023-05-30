#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and calculates fruits. """    
    
    # Create a socket and bind it to all available interfaces
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    sock.listen(1)
    
    while True:
        # Accept a connection and make a connection
        conn, addr = sock.accept()
        
        # Receive the fruit count
        fruit = conn.recv(1024)
        
        # Send the fruit count back to the client
        conn.sendall(fruit)
        
        # Close the connection
        conn.close()
        
        # Wait a little bit before continuing
        time.sleep(0.5)
        
