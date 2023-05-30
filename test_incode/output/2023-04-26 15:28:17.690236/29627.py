#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = str(self.path)
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/index.html':
                path = '/index.html'
            
            path = path.replace('//', '/')
            
            if path == '/':
                path = '/index.html'
            
            path = path.