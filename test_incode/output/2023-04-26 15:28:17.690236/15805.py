#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0 and port < 65535:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.send('Bye')
            conn.close()
            
        else:
            print('Port must be between 0 and 65535')
            
    else:
        print('Usage: python remove-port.py')
        
