#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or returns a port. """    
    port = int(input("Enter a port number: "))
    
    while True:
        print("Opening port {}".format(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        sock.send("Hello, world!")
        
        sock.close()
        
        print("Port closed")
        
        port = port + 1
        
        if port > 65535:
            port = 1
        
