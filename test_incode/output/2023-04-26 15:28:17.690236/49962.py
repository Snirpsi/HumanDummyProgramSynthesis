#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>User Input</title></head>'
                                    '<body><p>User input: </p></body></html>', 'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    