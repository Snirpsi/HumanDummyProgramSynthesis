#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    client, address = sock.accept()
    
    message = client.recv(1024)
    
    client.close()
    
    print(message)
    
    sock.close()
    
