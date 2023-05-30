#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the requested word """
            word = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(word.encode('utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting httpserver on port 8080')
    httpd.serve_forever()
    
