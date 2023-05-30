#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    print('Listening on port {}'.format(port))
    
    while True:
        client, addr = sock.accept()
        print('Got connection from {}'.format(addr))
        
        message = client.recv(1024)
        print('Received: "{}"'.format(message))
        
        client.send('