#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("0.0.0.0", port))
            sock.listen(1)
            sock.settimeout(1)
            
            conn, addr = sock.accept()
            
            conn.settimeout(1)
            
            conn.send("Hello, world!\n")
            conn.close()
            
        except socket.error as e:
            print("Socket error: {}".format(e))
            
        except KeyboardInterrupt:
            print("\nClosing port")
            
