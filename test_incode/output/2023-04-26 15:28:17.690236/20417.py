#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or adds a port. """    
    
    while True:
        
        port = int(input("Enter a port number: "))
        
        if port < 1024:
            print("Port number must be at least 1024")
        elif port > 65535:
            print("Port number must be at most 65535")
        else:
            break
    
    if port == -1:
        print("No port number was entered")
    else:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        
        print("Server listening on port {}".format(port))
        
        while True:
            
            client, addr = sock.accept()
            
            print("Connection from {}".format(addr))
            
            client.send("Hello World!")
            
            client.close()
            
