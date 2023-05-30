#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and opens numbers. """    
    
    ports = range(65536)
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("", port))
        
        sock.close()
        
    print("Done")
    
