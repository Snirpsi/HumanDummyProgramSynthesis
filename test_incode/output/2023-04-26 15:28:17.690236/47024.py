#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(
                '<html><head><title>Fruits</title></head>'
                '<body>'
                '<h1>Fruits</h1>'
                '<ul>'
                '<li><a href="fruits/apple">Apple</a></li>'
                '<li><a href="fruits/banana">Banana</a></li>'
                '<li><a href="fruits/cherry">Cherry</a></li>'
                '<li><a href="fruits/grape">Grape</a></li>'
                '</ul>'
                '</body></html>'
                )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()
    
