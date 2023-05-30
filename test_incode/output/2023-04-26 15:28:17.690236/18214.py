#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and opens words. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""<html><head><title>Enumerate numbers</title></head>
<body>
<table>
<tr><th>Number</th><th>Word</th></tr>
""")
            
            for num in range(1, 11):
                self.wfile.write("""<tr><td>%d</td><td>%s</td></tr>\n""" % (num, words[num]))
            
            self.wfile.write("""</table></body></html>""")
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting httpd on port 8080')
    httpd.serve_forever()
    
