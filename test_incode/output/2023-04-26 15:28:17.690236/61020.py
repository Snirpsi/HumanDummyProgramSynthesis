#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or converts numbers. """    
    
    import sys
    import socket
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    
    while True:
        connection, client_address = server_socket.accept()
        
        try:
            connection.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html>')
            connection.send('<body><h1>Welcome to my web server!</h1>')
            connection.send('<p>')
            
            if sys.argv[1] == '1':
                connection.send('The first number is: %s' % str(connection.recv(1024)))
            elif sys.argv[1] == '2':
                connection.send('The second number is: %s' % str(connection.recv(1024)))
            else:
                connection.send('The number you entered is not valid.')
            
            connection.send('</body></html>')
            
            connection.close()
            
        except socket.error as e:
            print("Error while accepting connection: %s" % e)
            
