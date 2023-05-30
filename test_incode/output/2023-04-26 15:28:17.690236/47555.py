#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port. """    
    while True:
        port = input('Enter a port to listen on: ')
        
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('localhost', int(port)))
            server.listen(1)
            
            conn, addr = server.accept()
            
            print('Connected by', addr)
            
            conn.send('