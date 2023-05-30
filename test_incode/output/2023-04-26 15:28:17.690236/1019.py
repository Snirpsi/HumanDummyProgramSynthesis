#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""
            <html><head><title>Converting numbers</title></head>
            <body>
            <h1>Converting numbers</h1>
            <p>
            Enter a number between 1 and 100: <input type='text' name='number'>
            </p>
            <form method='GET'>
            <input type='submit' value='Convert'>
            </form>
            </body></html>
            """)
    
    httpd = HTTPServer(('', port), Handler)
    print('Serving at port {}'.format(port))
    httpd.serve_forever()
    
