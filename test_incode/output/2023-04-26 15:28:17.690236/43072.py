#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    ports_to_remove = []
    for port in range(0, 65535):
        ports_to_remove.append(port)
    for port in ports_to_remove:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        while True:
            conn, addr = sock.accept()
            conn.close()
            print('Server listening on port ' + str(port))
            
