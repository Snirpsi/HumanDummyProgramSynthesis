#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    
    ports = range(0,65535)
    
    while True:
        for port in ports:
            print("Listening on port {}".format(port))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.settimeout(1.0)
            
            conn.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
            
            conn.close()
            
            
