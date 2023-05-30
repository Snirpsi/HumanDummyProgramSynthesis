#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    while True:
        
        # Wait for port to become available
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        sock.listen(1)
        print('Listening on port {}'.format(sock.getsockname()[1]))
        
        # Accept a connection and then start a thread
        connection, address = sock.accept()
        print('Connected by', address)
        t = threading.Thread(target=handle_connection, args=(connection, address))
        t.daemon = True
        t.start()
        
