#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and returns words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from multiprocessing import Process
    
    port = 8080
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Return index.html. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.index_html)
            elif parsed_url.path == '/multiply':
                """ Return words * words. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word1':
                """ Return word1 * word1. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word2':
                """ Return word1 * word2. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word3':
                """ Return word1 * word3. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word4':
                """ Return word1 * word4. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word5':
                """ Return word1 * word5. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word6':
                """ Return word1 * word6. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif parsed_url.path == '/multiply?words=word7':
                """ Return word1 * word7. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.multiply_html)
            elif 