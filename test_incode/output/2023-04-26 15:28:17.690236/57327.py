#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from json import dumps
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(dumps({'words': list(sys.argv[1:])}))
            else:
                self.send_error(404)
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting server')
    httpd.serve_forever()
    
