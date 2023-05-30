#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes a list of words.
    #This script is intended to be run from the command line.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from SocketServer import ThreadingTCPServer
    from subprocess import Popen, PIPE
    from shutil import copyfile
    
    
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Remove Words</title></head><body>"
                    "<center><h1>Remove Words</h1></center></body></html>",
                    "utf8"))
            elif path == "/remove":
                words = self.path.split("/")[1:]
                words = list(set(words))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Remove Words</title></head><body>"
                    "<center><h1>Remove Words</h1></center></body></html>",
                    "utf8"))
            elif path == "/remove/all":
                words = self.path.split("/")[1:]
                words = list(set(words))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Remove Words</title></head><body>"
                    "<center><h1>Remove Words</h1></center></body></html>",
                    "utf8"))
            else:
                self.send_error(404)
                self.end_headers()
                return
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

