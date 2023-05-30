#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port. """    
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        sock.listen(1)
        print('Listening on port {}'.format(sock.getsockname()[1]))
        
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            
            conn.send('Hello from Python!')
            
            conn.close()
            
