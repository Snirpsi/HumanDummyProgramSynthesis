#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that multiplies a list of words. """
        def do_GET(self):
            """ Handle a GET request. """
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            
            words = []
            for word in query['words']:
                words.append(word)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Multiplying Words</title></head>'
                '<body>'
                '<H1>Multiplying Words</H1>'
                '<H2>Enter a comma-separated list of words to multiply</H2>'
                '<form action="/multiply" method="GET">'
                '<textarea rows="10" cols="40" name="words" wrap="virtual"></textarea>'
                '<input type="submit" value="Submit">'
                '</form>'
                '</body></html>'
            )
    
    server = HTTPServer(('', 8080), RequestHandler)
    