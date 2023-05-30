#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            params = parse_qs(path)
            
            if path == '/':
                response = '<html>'
                response += '<head><title>Multiply</title></head>'
                response += '<body>'
                response += '<center><h1>Multiply</h1></center>'
                response += '<hr>'
                response += '<form action="/multiply" method="post">'
                response += '<input type="text" name="num1" value="0" />'
                response += '<input type="text" name="num2" value="0" />'
                response += '<input type="submit" value="Multiply" />'
                response += '</form>'
                response += '</body></html>'
                self.send_response(200)
                self.end_headers()
                self.wfile.write(response)
            else:
                num1 = params.get('num1')
                num2 = params.get('num2')
                
                if num1 and num2:
                    response = 'The product of %s and %s is %s.' % (num1, num2, num1*num2)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(response)
                else:
                    self.send_response(404)
                    self.end_headers()

    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

