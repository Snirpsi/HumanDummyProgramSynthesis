#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    
    class NumbersHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the numbers. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(self.server.numbers)
    
    server_address = ('', 8000)
    httpd = ThreadingMixIn(
        ThreadingMixIn.