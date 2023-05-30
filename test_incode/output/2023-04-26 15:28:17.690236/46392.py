#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, print_number)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver |>
<| a dscore=0 |>
