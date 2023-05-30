#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and returns fruits. """    
    
    while True:
        
        # Open a port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 5000))
        sock.listen(1)
        
        # Accept connection
        conn, addr = sock.accept()
        
        # Receive a message
        message = conn.recv(1024)
        
        # Send a message
        conn.send('Hello World!\n')
        
        # Close the connection
        conn.close()
        
        # Print the received message
        print(message)
        
        # Close the port
        sock.close()
        
        # Sleep for a second
        time.sleep(5)
        
