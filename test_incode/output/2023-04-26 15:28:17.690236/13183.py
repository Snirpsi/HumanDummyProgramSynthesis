#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '<html>\n<head>\n<title>Enumerate input</title>\n</head>\n<body>\n<form>\n<textarea name="input" rows="10" cols="40"></textarea>\n</form>\n</body>\n</html>'
            self.wfile.write(html.encode('utf8'))
    
    server = HTTPServer(("", 80), RequestHandler)
    server.serve_forever()
    
