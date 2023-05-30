#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Serving on port %s" % port)
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    
    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("""<html>
    <head>
        <title>Multiply two numbers</title>
    </head>
    <body>
        <h1>Multiply two numbers</h1>
        <form action="/" method="post">
            Enter the first number: <input type="text" name="firstnum">
            Enter the second number: <input type="text" name="secondnum">
            <input type="submit" value="Submit">
        </form>
    </body>
</html>""")
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %s" % port)
    httpd.serve_forever()
    
