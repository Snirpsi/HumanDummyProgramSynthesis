#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Get a GET request from the browser. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<h1>Hello world!</h1>', 'utf-8'))
            
    httpd = HTTPServer(('', 8080), RequestHandler)
    
    print('Serving on port 8080...')
    httpd.serve_forever()
