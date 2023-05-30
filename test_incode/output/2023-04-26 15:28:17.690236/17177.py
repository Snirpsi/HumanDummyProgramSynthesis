#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and removes fruits. """    
    
    # Start a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080/')
    
    # Wait for connections
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
