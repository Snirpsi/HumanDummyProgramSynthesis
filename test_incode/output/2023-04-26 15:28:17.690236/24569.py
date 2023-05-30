#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    
    client, addr = sock.accept()
    
    