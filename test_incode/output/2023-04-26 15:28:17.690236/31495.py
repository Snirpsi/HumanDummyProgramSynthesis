#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and enumerates numbers. """    
    
    # Start a server
    server = HTTPServer(('localhost', 8080), MyHandler)
    server.serve_forever()
    
    # Start a client and connect to it
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(('localhost', 8080))
    cli.send('GET / HTTP/1.0\r\nHost: localhost\r\n\r\n')
    
    # Read all data sent by the client
    while True:
        data = cli.recv(1024)
        if not data: break
        
        # Print received data
        print(data)
        
    # Close the connection
    cli.close()
    
    # Stop the server
    server.socket.close()
    
