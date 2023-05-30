#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or enumerates a list of words. """    
    import sys
    import webbrowser
    import http.server
    import socketserver

    httpd = socketserver.TCPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
    webbrowser.open('http://localhost:8000/')
    httpd.serve_forever()
    
<|/ file source=github |>