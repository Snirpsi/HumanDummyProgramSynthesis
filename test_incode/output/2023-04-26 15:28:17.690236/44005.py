#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or returns a list of numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python-3.x,python |>
<| c |>
Thanks for the answer. I am getting an error when I try to run the script as `python webserver.py`. The error is: `File "webserver.py", line 8, in <module>
    httpd = HTTPServer(('', port), FruitHandler)
  File "/usr/lib/python3.5/http/server.py", line 72, in __init__
    HTTPServer.__init__(self, server_address, RequestHandler)
  File "/usr/lib/python3.5/http/server.py", line 174, in __init__
    self.finish()
  File "/usr/lib/python3.5/http/server.py", line 206, in finish
    self.wfile.flush()
AttributeError: 'NoneType' object has no attribute 'flush'`
<|/ c |>
<| c |>
I edited the answer to fix the error. Try it again.
<|/ c |>
<| c |>
Thanks a lot! It worked! I didn't realize that `HTTPServer` was a class and not an instance of `HTTPServer`. I was trying to use `HTTPServer` as `httpd = HTTPServer(('', port), FruitHandler)` which was causing the error.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a |>
<code>
httpd = HTTPServer(('', port), FruitHandler)
</code>
This line creates a new instance of HTTPServer, which is probably not what you want.
<code>
httpd = HTTPServer((host, port), FruitHandler)
</code>
This line creates a new instance of HTTPServer, which is probably what you want.
<|/ a tags=python-3.x,python dscore=0 |>
<| c |>
Thanks for the answer. I am getting an error when I try to run the script as `python webserver.py`. The error is: `File "webserver.py", line 8, in <module>
    httpd = HTTPServer(('', port), FruitHandler)
  File "/usr/lib/python3.5/http/server.py", line 72, in __init__
    HTTPServer.__init__(self, server_address, RequestHandler)
  File "/usr/lib/python3.5/http/server.py", line 174, in __init__
    self.finish()
  File "/usr/lib/python3.5/http/server.py", line 206, in finish
    self.wfile.flush()
AttributeError: 'NoneType' object has no attribute 'flush'`
<|/ c |>
<| c |>
I edited the answer to fix the error. Try it again.
<|/ c |>
<|