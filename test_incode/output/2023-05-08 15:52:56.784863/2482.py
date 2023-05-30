#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of words.
    #It will listen on port 8080 and will respond to GET requests with the
    #list of words as JSON.
    import sys
    import socket
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import json

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            words = path.split("/")
            words = [word.lower() for word in words]
            words = [word for word in words if word]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            words = [word for word in words if word not in words]
            word

