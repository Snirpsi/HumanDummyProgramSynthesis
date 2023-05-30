#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers or multiplyes numbers. """    
    import sys
    import socketserver
    import cgi
    import math
    
    HOST, PORT = "localhost", 8000
    
    form = cgi.FieldStorage()
    
    if form.getvalue('number'):
        number = int(form.getvalue('number'))
        
        if form.getvalue('number') == '*':
            number = math.multiply(number, number)
            
        sys.stdout.write("<html><body>")
        sys.stdout.write("<h1>Hello, %s!</h1>" % cgi.escape(number))
        sys.stdout.write("</body></html>")
    else:
        sys.stdout.write("<html><body>")
        sys.stdout.write("<h1>Hello, world!</h1>")
        sys.stdout.write("</body></html>")
    
    httpd = socketserver.TCPServer((HOST, PORT), 