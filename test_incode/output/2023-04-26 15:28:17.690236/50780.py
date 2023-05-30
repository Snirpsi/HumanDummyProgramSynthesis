#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| a tags=python,webserver,python-3.x,sockets |>
Try this:
<code>
import socket
