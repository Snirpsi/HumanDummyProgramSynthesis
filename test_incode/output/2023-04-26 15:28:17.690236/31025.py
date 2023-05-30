#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers or enumerates fruits. """    
    
    # Start a server
    httpd = HTTPServer(('', 8000), FruitHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8000')
    
    # Wait for connection
    httpd.serve_forever()
    
