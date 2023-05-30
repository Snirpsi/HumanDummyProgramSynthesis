#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    ports = []
    
    # Open the ports we want to listen on
    for port in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('127.0.0.1', port))
        sock.listen(1)
        ports.append(port)
        
    # Now start listening for connections
    while True:
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        sock.close()
        
        # Wait for another connection
        sock, addr = sock.accept()
        print('Got connection from %s' % str(addr))
        
        # Do something with the connection
        sock.send('Hello World!')
        
        # Close the connection
        