#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or returns a list of words. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '--ports':
            ports = ports + list(range(65535))
        elif arg == '--port':
            ports.append(int(arg))
        else:
            ports.append(arg)
    
    ports.sort()
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        
        sock.setblocking(0)
        
        print('Listening on port {}'.format(port))
        
        while True:
            
            conn, addr = sock.accept()
            
            conn.setblocking(0)
            
            conn.send(b'Hello, world!')
            
            conn.close()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            