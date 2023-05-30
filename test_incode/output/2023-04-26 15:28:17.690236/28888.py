#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            words = []
            
            with open('words.txt') as file:
                for line in file:
                    line = line.strip()
                    
                    if line:
                        words.append(line)
            
            self.wfile.write(', '.join(words))
            
    server = HTTPServer(('', 8000), WordsHandler)
    
    print('Starting webserver on port 8000...')
    server.serve_forever()
    
