#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or iterates over user input. """    
    
    # start a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # start a web browser
    webbrowser.open('http://localhost:8080')
    
    # wait for user input
    server.serve_forever()
    
