#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    httpd = make_server('localhost', 8000, app)
    httpd.serve_forever()
</code>
<|/ a tags=python,flask,webserver |>
<| c |>
Thanks for your answer. 