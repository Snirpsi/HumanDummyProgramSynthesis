#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    # start a server
    server = HTTPServer(('', 80), WordsHandler)
    
    # start a web browser
    webbrowser.open('http://localhost:80')
    
    # wait for the server to start
    server.serve_forever()
    
