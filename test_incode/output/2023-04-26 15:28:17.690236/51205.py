#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and enumerates fruits. """    
    
    ports = [80, 8080, 8081, 8082, 8083, 8084, 8085]
    
    fruits = []
    for port in ports:
        fruits.append(Fruit(port))
    
    server = HTTPServer(('', 8080), FruitHandler)
    
    print('Serving on port 8080')
    
    server.serve_forever()
    
