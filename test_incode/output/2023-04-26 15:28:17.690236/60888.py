#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words and converts all ports. """    
    ports = range(65535)
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            conn, addr = sock.accept()
            conn.settimeout(1)
            conn.send('Hello, world!\n')
            conn.close()
            ports.remove(port)
            
