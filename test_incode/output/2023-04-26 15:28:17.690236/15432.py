#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    httpd = HTTPServer(('', 8000), WordsHandler)
    print('Starting httpd...')
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for the answer. 