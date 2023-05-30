#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and adds fruits. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    fruits = ['apple', 'orange', 'pear', 'banana', 'mango']
    
    for port in ports:
        server = HTTPServer(('', port), FruitServer)
        server.serve_forever()
        
    print('Server running at port %s' % port)
    
