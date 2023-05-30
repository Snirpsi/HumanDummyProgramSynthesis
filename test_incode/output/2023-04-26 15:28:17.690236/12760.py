#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and opens user input. """    
    
    # Start a server
    server = HTTPServer(('localhost', 8080), NumbersHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080')
    
    # Wait for input
    server.serve_forever()
    
