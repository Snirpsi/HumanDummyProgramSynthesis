#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and opens fruits. """    
    while True:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        conn, addr = sock.accept()
        print('Connected by', addr)
        conn.send('Hello, world!')
        conn.close()
        
