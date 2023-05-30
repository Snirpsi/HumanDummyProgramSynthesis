#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    
    port = int(sys.argv[1])
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', port))
    server.listen(1)
    
    while True:
        client, addr = server.accept()
        print('Connected by', addr)
        
        client.send('Hello World!')
        client.close()
        
