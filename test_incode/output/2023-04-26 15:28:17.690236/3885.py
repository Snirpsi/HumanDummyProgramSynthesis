#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the numbers. """
            
            numbers = []
            
            for i in range(10):
                numbers.append(i)
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write('<html><body>')
            self.wfile.write('<table>')
            self.wfile.write('<tr><th>Number</th><th>Result</th></tr>')
            
            for number in numbers:
                self.wfile.write('<tr><td>%d</td><td>%s</td></tr>' % (number, number))
            
            self.wfile.write('</table></body></html>')
            
    httpd = HTTPServer(("", port), MyHandler)
    print('Serving on port %s' % port)
    httpd.serve_forever()
    
