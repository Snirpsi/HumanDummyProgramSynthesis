#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and opens fruits. """    
    
    # Start a server
    server = HTTPServer(('', 8080), FruitHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080/')
    
    # Wait for connection
    server.serve_forever()
    
