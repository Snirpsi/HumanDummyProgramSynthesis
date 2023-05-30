#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that iterates over a list of numbers.
    #The server will respond with an HTML page that lists the numbers in 
    #the list.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import cgi
    import os
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            
            if path == '/':
                html = '<html>'
                html += '<head><title>List of numbers</title></head>'
                html += '<body>'
                html += '<p> List of numbers: </p>'
                html += '<ul>'
                for number in numbers:
                    html += '<li>' + str(number) + '</li>'
                html += '</ul>'
                html += '</body>'
                html += '</html>'
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html)
            else:
                html = '<html>'
                html += '<head><title>List of numbers</title></head>'
                html += '<body>'
                html += '<p> List of numbers: </p>'
                html += '<ul>'
                for number in numbers:
                    html += '<li>' + str(number) + '</li>'
                html += '</ul>'
                html += '</body>'
                html += '</html>'
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html)
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()

