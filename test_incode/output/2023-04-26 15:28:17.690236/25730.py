#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input("Enter a port number: ")
        
        # Open a socket to listen for connections.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', int(port)))
        sock.listen(1)
        
        # Accept the connection and make a file-like object out of it.
        conn, addr = sock.accept()
        
        # Read a line from the connection.
        line = conn.recv(1024).decode()
        
        # Send the line back to the client.
        conn.sendall(line.encode())
        
        # Close the connection.
        conn.close()
        
        # Wait a little bit before trying again, just in case.
        time.sleep(0.1)
