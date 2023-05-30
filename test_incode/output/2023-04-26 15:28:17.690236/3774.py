#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/proc/net/tcp').read().splitlines()
    ports = [int(p) for p in ports if p.isdigit()]
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        
        sock.setblocking(0)
        
        clients = []
        
        while 1:
            client, addr = sock.accept()
            clients.append(client)
            
            client.send('Hello, world!\n')
            
            client.close()
            
            
if __name__ == '__main__':
    main()