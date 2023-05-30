#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,port,python-3.x |>
<| c |>
Thank you, this is exactly what I was looking for.
<|/ c |>
<| a dscore=0 |>
<code>
