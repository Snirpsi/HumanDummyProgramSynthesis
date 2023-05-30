#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    from multiprocessing import Process
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request to the server. """
            
            q = parse_qs(urlparse(self.path).query)
            
            if q['op'] == 'multiply':
                words = [w.strip() for w in q['words']]
                
                p = Process(target=multiply, args=(words,))
                p.start()
                
                self.send_response(200)
                self.end_headers()
                
            else:
                self.send_error(405, 'Invalid operation')
                
    httpd = HTTPServer(("", 8080), Handler)
    httpd.serve_forever()
