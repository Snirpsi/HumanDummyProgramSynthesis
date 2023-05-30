#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '<html>'
            html += '<head><title>Enumerate user input</title></head>'
            html += '<body>'
            html += '<p> Enter a number: </p>'
            html += '<p> Enter a letter: </p>'
            html += '<p> Enter a word: </p>'
            html += '</body></html>'
            
            self.wfile.write(bytes(html, 'utf8'))
    
    server = HTTPServer(('', 8080), Handler)
    
    print('Server running at http://127.0.0.1:8080/')
    
    server.serve_forever()
    
