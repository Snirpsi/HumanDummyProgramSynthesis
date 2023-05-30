#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns numbers and opens all ports. """    
    ports = range(1,65535)
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port {}'.format(port))
        
        while True:
            client, addr = sock.accept()
            print('Connected by', addr)
            
            client.send('