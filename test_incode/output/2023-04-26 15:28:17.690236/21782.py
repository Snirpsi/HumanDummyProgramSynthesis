#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and iterates over numbers. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('',port))
            sock.listen(1)
            
            client, address = sock.accept()
            
            client.close()
            
            sock.close()
            
        ports.remove(port