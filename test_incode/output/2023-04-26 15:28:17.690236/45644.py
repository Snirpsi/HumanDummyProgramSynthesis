#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and opens fruits. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", port))
        
        print("Opening fruit on port {}".format(port))
        
        sock.send("Hello, world!")
        
        sock.close()
        
        print("Closing fruit on port {}".format(port))
        
    
