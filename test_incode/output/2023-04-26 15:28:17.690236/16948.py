#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port. """    
    port = sys.argv[1]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        print('Connected by', addr)
        
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            client.send(data)
            
        client.close()
        
    sock.close()

<|/ file source=github |>