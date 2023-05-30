#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    from io import StringIO
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple handler that adds a list of numbers. """
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                s = StringIO()
                s.write('<html><body>')
                s.write('<ol>\n')
                s.write('<li>')
                s.write('<ol>\n')
                
                for num in range(1, 11):
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('<li>')
                    s.write('<ol>\n')
                    
                    s.write('