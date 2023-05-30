#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    # Start a server
    server = HTTPServer(("", 80), FruitHandler)
    
    # Start a web browser
    webbrowser.open("http://localhost:80/")
    
    # Wait for user input
    server.serve_forever()
    
