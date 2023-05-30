#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import os
    import socket
    import webbrowser
    
    port = int(os.getenv('PORT', 8080))
    
    server_socket = socket.socket()
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    
    webbrowser.open('http://localhost:8080')
    
    while True:
        connection, client_address = server_socket.accept()
        
        connection.send('HTTP/1.1 200 OK\r\n')
        connection.send('Content-Type: text/plain\r\n')
        connection.send('\r\n')
        
        connection.send(''.join(['<html><body>',
                                  '<ol>',
                                  '  <li>',
                                  '    ',
                                  '    ',
                                  '    ',
                                  '    ',
                                  '  </li>',
                                  '</ol>',
                                  '</body></html>']))
        
        connection.close()
        
