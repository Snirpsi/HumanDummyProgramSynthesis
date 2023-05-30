#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    # Open a port and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8001))
    sock.listen(1)
    
    # Accept connections
    while True:
        conn, addr = sock.accept()
        print('Connection from', addr)
        
        # Receive data from client
        data = conn.recv(1024)
        print('Received data from client:', data)
        
        # Send data to client
        conn.sendall(b'Hello, world!\n')
        
        # Close connection
        conn.close()
        
        # Wait for next connection
        conn.recv(1024)
        
        # Close socket
        sock.close()
