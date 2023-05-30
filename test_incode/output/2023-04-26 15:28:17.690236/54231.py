#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port and calculates numbers. """    
    while True:
        port = random.randint(1, 65535)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        conn, addr = sock.accept()
        conn.send('Hello, world!\n')
        conn.close()
        
