#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and removes a port. """    
    port = 8080
    httpd = make_server('localhost', port, app)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
</code>
<|/ a tags=python,flask,webserver |>
<| c |>
Thanks for your answer. 