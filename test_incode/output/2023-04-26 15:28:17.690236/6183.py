#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and returns all ports. """    
    
    ports = []
    
    # Open ports one by one
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        ports.append(port)
        
    # Open all ports
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
    # Wait until all clients connect
    while True:
        client, addr = sock.accept()
        print('Got connection from %s:%d' % (addr[0], addr[1]))
        
        # Receive a request from client
        data = client.recv(1024)
        
        # Send response to client
        client