#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or stores user input. """    
    while True:
        try:
            port = int(input("Enter a port number to listen to: "))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            print("Connected by", addr)
            
            while True:
                
                data = conn.recv(1024)
                if not data:
                    break
                
                conn.sendall(data)
                
            conn.close()
            
        except KeyboardInterrupt:
            
            break
            
