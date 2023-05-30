#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and prints all ports. """    
    
    ports = range(5000, 5999)
    
    server_address = ('', 5000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    print('Starting server')
    httpd.serve_forever()
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server')
    httpd.socket.close()
    
    print('Stopping server')
    httpd.socket.shutdown(socket.SHUT_RDWR)
    
    print('Stopping server