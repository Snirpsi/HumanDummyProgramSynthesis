#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    httpd = HTTPServer(('localhost', 8000), WordsHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks, I 