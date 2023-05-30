#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import socketserver
    
    class EchoHandler(socketserver.BaseRequestHandler):
        def handle(self):
            """ Handle the request. """
            data = self.request.recv(1024).strip()
            self.request.sendall(str(data) * '\n')
    
    httpd = socketserver.TCPServer(("", 8080), EchoHandler)
    httpd.serve_forever()