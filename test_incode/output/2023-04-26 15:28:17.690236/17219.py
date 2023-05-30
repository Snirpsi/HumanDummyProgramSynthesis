#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing out the words. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><head><title>Enumerate Words</title></head>'
                                    '<body><p>Enumerate words: %s</p></body></html>'
                                    % ', '.join(self.words),
                                    'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpd on', server_address)
    httpd.serve_forever()
    
