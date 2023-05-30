#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and enumerates user input. """    
    
    ports = input("Enter ports: ")
    
    for port in ports.split(","):
        
        try:
            
            port = int(port)
            
            if port > 0 and port <= 65535:
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(("0.0.0.0", port))
                sock.listen(1)
                
                while True:
                    
                    conn, addr = sock.accept()
                    
                    data = conn.recv(1024)
                    
                    conn.send(data)
                    
                    conn.close()
                    
            else:
                
                print("Port number must be between 0 and 65535.")
                
        except ValueError as 