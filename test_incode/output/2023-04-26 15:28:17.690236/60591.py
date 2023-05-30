#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    port = 8000
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=0 tags=python,webserver,ports |>
<| c |>
Thanks, this works great!
<|/ c |>
<| c |>
You're welcome. Don't forget to accept the answer if it helped you.
<|/ c |>
<| c |>
I did but 