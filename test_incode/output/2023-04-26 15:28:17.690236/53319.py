#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    ports.sort()
    
    for port in ports:
        print('Port {} is listening on {}'.format(port,
            ', '.join(['http://127.0.0.1:{}'.format(port)])))
    
