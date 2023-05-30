#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port. """    
    while True:
        port = random.randint(10000, 65535)
        print("Starting port {} ...".format(port))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        client, addr = sock.accept()
        print("Got connection from {}".format(addr))
        
        