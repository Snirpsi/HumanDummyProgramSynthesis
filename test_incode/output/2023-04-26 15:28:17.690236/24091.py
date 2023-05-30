#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    port = 8080
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. Unfortunately this doesn't work. I get the following error when trying to run the server: 
`Traceback (most recent call last):
  File "/home/ubuntu/workspace/portremover/server.py", line 13, in <module>
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
  File "/usr/lib/python3.4/http/server.py", line 76, in __init__
    self.server_name = server_address
AttributeError: 'tuple' object has no attribute 'server_name'`
<|/ c |>
<| c |>
