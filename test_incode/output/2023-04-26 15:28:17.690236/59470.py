#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(10)
            
            for number in numbers:
                self.wfile.write(str(number))
                self.wfile.write('<br>')
            
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            
            self.wfile.write('<hr>')
            self.wfile.write('<br>')
            