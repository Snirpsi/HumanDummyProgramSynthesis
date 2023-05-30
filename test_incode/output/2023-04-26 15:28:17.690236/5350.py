#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and calculates numbers. """    
    
    # Start a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080/')
    
    # Wait for connections
    server.serve_forever()
    
