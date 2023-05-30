#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports or converts fruits. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi']
    
    for port in ports:
        httpd = make_server(port, fruits)
        httpd.serve_forever()
    
