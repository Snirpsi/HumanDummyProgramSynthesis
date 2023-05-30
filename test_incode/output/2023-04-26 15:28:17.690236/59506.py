#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input and opens a port. """    
    while True:
        port = input('Enter a port number: ')
        
        try:
            port = int(port)
        except ValueError:
            print('Invalid port number')
            continue
        
        print('Opening port {}'.format(port))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(1)
            
            print('Listening on port {}'.format(port))
            
            conn, addr = sock.accept()
            
            print('Connected by', addr)
            
            conn.send('Hello, world!\n')
            
            conn.close()
            
        except KeyboardInterrupt:
            print('\nBye!')
            
            break
            
        except:
            print('\nSomething went wrong.')
            
            break
            
        finally:
            sock.close()
            
