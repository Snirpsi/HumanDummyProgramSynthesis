#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        
        data = conn.recv(1024)
        if not data:
            break
        
        conn.send(data)
        
        conn.close()
        
    print('Closing port', port)
    sock.close()
    
