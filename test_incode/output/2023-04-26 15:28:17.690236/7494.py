#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            words = sys.argv[1:]
            
            for word in words:
                self.wfile.write(str(word))
                
    httpd = HTTPServer(('', 8080), RequestHandler)
    print('Serving on port 8080')
    httpd.serve_forever()
    
