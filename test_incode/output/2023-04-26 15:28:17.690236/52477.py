#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers or opens all ports. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! It works perfectly!
<|/ c |>
<| c |>
