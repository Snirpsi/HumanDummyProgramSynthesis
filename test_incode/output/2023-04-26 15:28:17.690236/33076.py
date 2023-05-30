#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that enumerates fruits. """
        
        def do_GET(self):
            """ Responds to GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Fruits</title></head>'
                '<body>'
                '<table>'
                '<tr><th>Name</th><th>Description</th></tr>'
                '<tr><td>Apple</td><td>A fruit of fruit.</td></tr>'
                '<tr><td>Banana</td><td>A fruit of fruit.</td></tr>'
                '<tr><td>Orange</td><td>A fruit of fruit.</td></tr>'
                '<tr><td>Pear</td><td>A fruit of fruit.</td></tr>'
                '</table>'
                '</body></html>'
                )
    
    
    
    server = HTTPServer(('', 8000), FruitHandler)
    