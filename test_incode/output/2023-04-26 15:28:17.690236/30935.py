#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port. """    
    port = int(sys.argv[1])
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        client, addr = sock.accept()
        print('Got connection from ', addr)
        while True:
            data = client.recv(1024)
            if not data:
                break
            client.sendall(data)
        client.close()
        sock.close()
        print('Closing socket')
        break
