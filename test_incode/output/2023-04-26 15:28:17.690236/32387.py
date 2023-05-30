#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data:
            break
        print('Received', repr(data))
        conn.sendall(data)
        conn.close()
    
    sock.close()
    
