#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and enumerates all ports. """    
    
    ports = []
    
    server = HTTPServer(('', 0), MyHandler)
    
    ports.append(server.socket.getsockname()[1])
    
    print('Starting webserver')
    
    server.serve_forever()
    
    print('Stopping webserver')
    
    server.socket.close()
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_WR)
    
    print('Stopped webserver')
    
    server.socket.close()
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.close()
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.close()
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.close()
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopped webserver')
    
    server.socket.shutdown(socket.