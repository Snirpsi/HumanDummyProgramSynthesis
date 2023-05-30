#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input("Enter a port number: ")
        
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        
        if port < 0 or port > 65535:
            print("Invalid port number")
            continue
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", port))
        
        print("Connected")
        
        sock.send("Hello, world!")
        
        sock.close()
        
        print("Disconnected")
        
        
