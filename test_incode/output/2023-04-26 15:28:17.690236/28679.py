#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            print("Connected by", addr)
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                conn.send(data)
                
            conn.close()
            
        except socket.error as e:
            print("Error connecting: ", e)
            
        except KeyboardInterrupt:
            print("\nBye!")
            
        finally:
            sock.close()
            
