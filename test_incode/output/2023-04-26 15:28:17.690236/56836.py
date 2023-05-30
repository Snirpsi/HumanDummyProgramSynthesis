#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), UserInputHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080')
    
    # Run the server
    server.serve_forever()
