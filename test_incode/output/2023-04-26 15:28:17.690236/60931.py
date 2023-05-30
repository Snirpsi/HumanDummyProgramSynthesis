#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    from io import StringIO
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Get a GET request from the browser. """
            
            query = parse_qs(urlparse(self.path).query)
            
            words = []
            for word in query['words']:
                words.append(word.strip())
            
            words = list(set(words))
            
            buf = StringIO()
            for word in words:
                buf.write('%s<br>' % word)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(buf.getvalue())
            
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print('Server stopped')

<|/ file ext=.py filename=server.py |>