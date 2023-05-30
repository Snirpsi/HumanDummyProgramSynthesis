#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = 5000
    
    # Create a socket and bind to port 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    # Accept connections from clients
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received', repr(data))
        conn.close()
        
    sock.close()
    
