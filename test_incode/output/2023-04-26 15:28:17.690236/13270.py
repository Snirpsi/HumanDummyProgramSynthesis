#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    
    port = 5000
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        client.send('Hello World!')
        client.close()
        
