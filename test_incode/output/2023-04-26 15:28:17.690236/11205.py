#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port and opens numbers. """    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    client, addr = sock.accept()
    
    message = client.recv(1024)
    
    client.close()
    
    print(message)
    
    sock.close()
    
