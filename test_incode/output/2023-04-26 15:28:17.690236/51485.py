#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and iterates over all ports. """    
    
    port = 8080
    
    # start a server
    server = HTTPServer(('', port), MyHandler)
    
    # start a web browser
    webbrowser.open('http://localhost:8080')
    
    # start a web server
    webserver.serve_forever()
    
