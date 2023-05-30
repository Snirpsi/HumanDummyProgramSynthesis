#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input or calculates words. """    
    
    # Start a server
    server = HTTPServer(('', 8000), Handler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8000')
    
    # Wait for user input
    server.serve_forever()

<|/ file source=github ext=.py |>