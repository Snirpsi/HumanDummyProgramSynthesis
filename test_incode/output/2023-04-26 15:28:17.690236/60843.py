#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports. """    
    ports = glob.glob('/sys/class/net/*/tcp/*/*/')
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', int(port)))
        sock.listen(1)
        print('Listening on port %s' % port)
        client, addr = sock.accept()
        print('Connected by', addr)
        client.send('Hello, world!')
        client.close()
        sock.close()
