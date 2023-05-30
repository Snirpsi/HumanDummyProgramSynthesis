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
            
            self.wfile.write(
                "<html><head><title>Enumerate numbers</title></head>"
                "<body><p>Enumerate numbers:</p>"
                "<table>"
                "<tr><th>Number</th><th>Description</th></tr>"
                "<tr><td>1</td><td>One</td></tr>"
                "<tr><td>2</td><td>Two</td></tr>"
                "<tr><td>3</td><td>Three</td></tr>"
                "<tr><td>4</td><td>Four</td></tr>"
                "<tr><td>5</td><td>Five</td></tr>"
                "<tr><td>6</td><td>Six</td></tr>"
                "<tr><td>7</td><td>Seven</td></tr>"
                "<tr><td>8</td><td>Eight</td></tr>"
                "<tr><td>9</td><td>Nine</td></tr>"
                "</table>"
                "</body></html>"
                )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting httpd on', server_address)
    httpd.serve_forever()

<|/ file source=github filename=