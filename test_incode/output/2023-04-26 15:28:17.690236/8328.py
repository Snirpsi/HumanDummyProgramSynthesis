#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and returns fruits. """    
    
    fruits = []
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        connection, address = sock.accept()
        
        data = connection.recv(1024)
        
        if data:
            fruits.append(data.decode())
        
        connection.close()
    
    sock.close()
    
    return fruits
    
