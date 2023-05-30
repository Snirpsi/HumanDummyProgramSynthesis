#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or returns user input. """    
    
    # Start a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start a web browser
    webbrowser.open('http://localhost:8080/words')
    
    # Run the server
    server.serve_forever()
    
