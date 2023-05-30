#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    
    port = 5000
    
    while True:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        sock.send("Hello World!")
        
        sock.close()
        
        print("Sent Hello World!")
        
        port = port + 1
        
        if port > 65535:
            port = 1
            
