#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        
        client, addr = sock.accept()
        print('Connected by', addr)
        
        buf = client.recv(1024)
        print('Received', buf)
        
        