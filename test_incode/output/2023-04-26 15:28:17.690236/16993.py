#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port == -1:
            print("\nExiting...\n")
            break
        else:
            print("\nRemoving port {}...".format(port))
            
            sock.close()
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("", port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            print("\nConnected to", addr)
            
            conn.sendall("Goodbye!")
            
            conn.close()
            
            sock.close()
            
            
