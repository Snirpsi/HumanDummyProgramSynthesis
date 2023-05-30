#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    print('Listening on port {}'.format(port))
    
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        client.send('Hello, world!\n')
        
        client.close()
        
