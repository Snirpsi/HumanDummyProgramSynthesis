#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over all ports and opens numbers. """    
    
    ports = range(1,65535)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        
        sock.send("Hello World!")
        
        sock.close()
        
        print("Port {} is opened.".format(port))
        
