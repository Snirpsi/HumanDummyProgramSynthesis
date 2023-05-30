#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the contents of the 
                GET request. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(self.rfile.read().decode())
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
    
