#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and opens fruits. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", port))
        
        sock.send("GET / HTTP/1.0\r\n\r\n".encode())
        
        sock.close()
        
        print("Port {} opened".format(port))
        
