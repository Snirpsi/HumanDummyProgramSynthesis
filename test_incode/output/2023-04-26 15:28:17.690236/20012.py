#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(10000, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        conn, addr = sock.accept()
        print('Got connection from', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)
        print('Connection closed')
        conn.close()
        
        
