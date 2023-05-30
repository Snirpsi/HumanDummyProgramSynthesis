#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and iterates over a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs, urlparse
    import math
    
    
    class NumberHandler(BaseHTTPRequestHandler):
        """ A simple handler for numbers. """
        
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Show the list of numbers. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    """
                    <html><head><title>List of numbers</title></head>
                    <body>
                    <p>List of numbers:</p>
                    <table border="1">
                    <tr><th>Number</th><th>Description</th></tr>
                    """)
                
                for number in sorted(math.factorial(n) for n in range(1, int(parsed_url.query.get('n', 1))+1)):
                    self.wfile.write(
                        """
                        <tr><td>%s</td><td>%s</td></tr>
                        """ % (number, str(math.factorial(number))))
                
                self.wfile.write(
                    """
                    </table>
                    </body>
                    </html>
                    """)
                
            elif parsed_url.path == '/numbers':
                """ Show the list of numbers. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    """
                    <html><head><title>List of numbers</title></head>
                    <body>
                    <p>List of numbers:</p>
                    <table border="1">
                    <tr><th>Number</th><th>Description</th></tr>
                    """)
                
                for number in sorted(math.factorial(n) for n in range(1, int(parsed_url.query.get('n', 1))+1)):
                    self.wfile.write(
                        """
                        <tr><td>%s</td><td>%s</td></tr>
                        """ % (number, str(math.factorial(number))))
                
                self.wfile.write(
                    """
                    </table>
                    </body>
                    </html>
                    """)
                
            elif parsed_url.path == '/numbers/<int:n>':
                """ Show the description of a number. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(
                    """
                    <html><head><title>Description of number %s</title></head>
                    <body>
                    <p>Description of number %s:</p>
                    <p>%s</p>
                    </body>
                    </html>
                    """ % (
                        number,
                        number,
                        str(math.factorial(number))
                    ))
                
            elif parsed_url.path == '/numbers/<int:n>/<int:d>