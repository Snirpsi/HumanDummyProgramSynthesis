#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import parse_qs, urlparse
    import socketserver
    
    HOST, PORT = "localhost", 8080
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler """
        def do_GET(self):
            """ Handle a GET request """
            query = parse_qs(urlparse(self.path).query)
            
            if query.get('q'):
                query = query['q']
                
                words = query.split()
                
                words = [w.capitalize() for w in words]
                
                response = "\n".join(words)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(response.encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                
    httpd = HTTPServer(('', PORT), RequestHandler)
    
    print("Serving at http://%s:%s" % (HOST, PORT))
    httpd.serve_forever()
    
