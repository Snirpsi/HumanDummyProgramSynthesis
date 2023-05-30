#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import StringIO
    
    class WordHandler(BaseHTTPRequestHandler):
        """ A simple handler for words. """
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Handle the root path. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    """
                    <html>
                        <head><title>Words</title></head>
                        <body>
                            <h1>Words</h1>
                            <p>Here are some words: </p>
                            <ul>
                                <li>Python</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python3</li>
                                <li>Python2</li>
                                <li>Python