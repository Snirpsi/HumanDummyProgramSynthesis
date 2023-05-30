#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class WordListHandler(BaseHTTPRequestHandler):
        """ A simple handler for our list of words. """
        
        def do_GET(self):
            """ Respond to a GET request by printing the list of words. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.writelines([word.upper() for word in open('wordlist.txt').read().splitlines()])
    
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WordListHandler)
    
    print('Starting httpserver on port 8000...')
    httpd.serve_forever()
