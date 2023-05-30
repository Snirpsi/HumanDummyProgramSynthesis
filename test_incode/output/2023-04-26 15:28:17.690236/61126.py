#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or converts a list of numbers. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import parse_qs, urlparse
    from sys import exit
    
    class FruitHandler(BaseHTTPRequestHandler):
        """ A handler for requests. """
        def do_GET(self):
            """ Handle a GET request. """
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            
            fruits = query['fruits']
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Fruits</title></head><body>'
                '<table>'
                '<tr><th>Fruit</th><th>Count</th></tr>'
                '<tr><td>Apple</td><td>1</td></tr>'
                '<tr><td>Banana</td><td>2</td></tr>'
                '<tr><td>Orange</td><td>3</td></tr>'
                '</table></body></html>'
                )
            
    
    
    server = HTTPServer(('', 8080), FruitHandler)
    
    server.serve_forever()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    