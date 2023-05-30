#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and multiplyes fruits. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    fruits = ['apple', 'orange', 'banana', 'kiwi', 'grape', 'mango']
    
    for port in ports:
        webserver.serve_forever(port=port)
    
    for fruit in fruits:
        webserver.serve_forever(port=port, fruit=fruit)
    
    webserver.server_close()
    
