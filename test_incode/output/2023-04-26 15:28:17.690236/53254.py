#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = []
    
    # Add port to list
    ports.append(8080)
    
    # Start server
    httpd = HTTPServer(('', 0), Handler)
    
    # Start server
    httpd.serve_forever()
    
    # Stop server
    httpd.socket.close()
    
    # Print ports
    print('Ports:')
    for port in ports:
        print('  ', port)
    
    # 