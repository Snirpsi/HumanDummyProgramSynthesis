#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import math
    import random
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request to /"""
            
            words = self.path.split('/')
            
            words = [word.strip() for word in words]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word]
            
            words = [word 