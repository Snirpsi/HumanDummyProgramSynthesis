#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        port = input('Enter the port to listen on: ')
        
        try:
            server = socket.socket()
            server.bind(('0.0.0.0', int(port)))
            server.listen(1)
            
            print('Listening on port ' + str(port))
            
            conn, addr = server.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello World!')
            
            conn.close()
            
        except socket.error as e:
            print('Port ' + str(port) + ' is already in use')
            
