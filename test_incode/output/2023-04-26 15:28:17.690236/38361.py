#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or adds a list of numbers. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><body>')
            self.wfile.write('<p> Available ports: </p>')
            self.wfile.write('<table>')
            for port in range(0, 65535):
                self.wfile.write('<tr><td>'+str(port)+'</td><td><a href="javascript:void(0)" onclick="openPort(\''+str(port)+'\')">Open</a></td></tr>')
            self.wfile.write('</table>')
            self.wfile.write('</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
