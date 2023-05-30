#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import math

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            words = parse_qs(
                self.path.split('?')[1]).get('words', [])
            
            words = [w.strip() for w in words]
            
            words = [w for w in words if w]
            
            words = [w for w in words if not math.isnan(w)]
            
            words = [w for w in words if len(w) > 2]
            
            words = [w for w in words if len(w) == 2]
            
            words = [w for w in words if len(w) == 1]
            
            words = [w for w in words if len(w) > 1]
            
            words = [w for w in words if w != '']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in words if w != ' ']
            
            words = [w for w in word