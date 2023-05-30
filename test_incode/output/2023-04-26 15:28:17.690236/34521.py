#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            words = self.path.split('/')
            
            words = [word.strip() for word in words]
            
            words = [word for word in words if word]
            
            words = [word for word in words if word.isalpha()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isspace()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isupper()]
            
            words = [word for word in words if word.islower()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalpha()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isspace()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isupper()]
            
            words = [word for word in words if word.islower()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalpha()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isspace()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isupper()]
            
            words = [word for word in words if word.islower()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalpha()]
            
            words = [word for word in words if word.isdigit()]
            
            words = [word for word in words if word.isalnum()]
            
            words = [word for word in words if word.isspace()]
            
            words = [word for word in words if word.isalnum()]
