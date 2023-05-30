#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class WebServer(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing all available ports. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            for port in range(1, 65535):
                print("Port {} is available at http://127.0.0.1:{}".format(port, port))
                
    httpd = HTTPServer(("", 0), WebServer)
    httpd.serve_forever()
    
