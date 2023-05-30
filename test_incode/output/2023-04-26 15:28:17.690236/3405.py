#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    
    while True:
        client, addr = sock.accept()
        print('Got connection from', addr)
        client.send('Hello, world')
        client.close()
        
    sock.close()
    
