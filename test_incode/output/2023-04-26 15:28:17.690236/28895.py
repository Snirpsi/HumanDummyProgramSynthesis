#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['80', '443']
    
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', int(port)))
        sock.listen(1)
        
        print('Listening on port 