#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import socketserver

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>Enumerate numbers</title></head>'
                                    '<body><p>Enumerate numbers:</p>'
                                    '<ol><li>', 'utf-8'))
            
            numbers = range(int(sys.argv[1]))
            
            for number in numbers:
                self.wfile.write(str(number))
                self.wfile.write('</li><li>')
            
            self.wfile.write(bytes('</ol></body></html>', 'utf-8'))
            
    httpd = socketserver.TCPServer(("", 80), MyHandler)
    print("Serving on port 80")
    httpd.serve_forever()
    
