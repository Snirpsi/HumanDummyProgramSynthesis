#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or multiplyes numbers. """    
    
    while True:
        port = random.randint(1, 65535)
        
        print("Opening port {}".format(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        conn, addr = sock.accept()
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.send(data * 2)
        
        conn.close()
        
        sock.close()
        
        print("Closing port {}".format(port))
        
