#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or opens words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver
    
    HOST, PORT = "localhost", 8000
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing out the numbers or words. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(10)
            words = ("word%d" % i for i in range(10))
            
            self.wfile.write(bytes(
                "<html><body>"
                "<table><tr><th>Number</th><th>Word</th></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"
                "<tr><td>", "</td><td></td></tr>"