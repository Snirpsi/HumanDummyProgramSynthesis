#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    
    class WordListHandler(BaseHTTPRequestHandler):
        """ A simple handler for printing words. """
        def do_GET(self):
            """ Handle a GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server.wordlist)
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordListHandler)
    httpd.serve_forever()
    
