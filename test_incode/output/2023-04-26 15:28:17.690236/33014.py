#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and iterates over all ports. """    
    
    port = int(sys.argv[1])
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        connection.send('HTTP/1.1 200 OK\r\n')
        connection.send('Content-Type: text/html\r\n')
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.send('<html><body><h1>Numbers</h1></body></html>\r\n')
        
        connection.send('\r\n')
        
        connection.