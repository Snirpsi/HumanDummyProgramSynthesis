#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and enumerates all ports. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), FruitServer)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080')
    
    # Run the server
    server.serve_forever()
    
