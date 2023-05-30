#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and calculates all ports. """    
    
    ports = [8080, 8081, 8082]
    fruits = ['apple', 'banana', 'cherry']
    
    # Create a server that prints fruits and all ports
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start a server
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
    # Print the fruits on the server
    print('Fruits:')
    for fruit in fruits:
        print('    ' + fruit)
    
    # Print the ports on the server
    print('Ports:')
    for port in ports:
        print('    ' + port)
    
    print('\nPress Ctrl+C to exit')
    
