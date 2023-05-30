#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or opens numbers. """    
    while True:
        port = int(input('Enter a port number: '))
        if port == -1:
            break
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        
        while True:
            conn, addr = sock.accept()
            print('Connected by', addr)
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
            
            conn.close()
            
