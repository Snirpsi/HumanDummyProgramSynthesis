#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Fruits</title>
            <style>
            body {
                font-family: sans-serif;
                font-size: 18px;
                line-height: 1.5;
                color: #333;
                padding: 0 20px;
            }
            
            h1 {
                font-size: 24px;
                font-weight: normal;
                margin: 0 0 20px;
            }
            
            h2 {
                font-size: 18px;
                font-weight: normal;
                margin: 0 0 20px;
            }
            
            h3 {
                font-size: 16px;
                font-weight: normal;
                margin: 0 0 20px;
            }
            
            p {
                margin: 0 0 20px;
            }
            
            a {
                color: #4183c4;
                text-decoration: none;
            }
            
            a:hover {
                text-decoration: underline;
            }
            </style>
            </head>
            <body>
            <h1>Fruits</h1>
            <ul>
            """)
            
            for fruit in sorted(Fruit.__subclasses__()):
                self.wfile.write(f"""
                <li><a href="{fruit.__module__}.{fruit.__name__}.html">{fruit.__name__}</a></li>
            """)
            self.wfile.write(f"""
            </ul>
            </body>
            </html>
            """)
    
    httpd = HTTPServer(("", 80), FruitHandler)
    httpd.serve_forever()
    
