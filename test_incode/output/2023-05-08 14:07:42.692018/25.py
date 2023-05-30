#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that opens a list of words.
    httpd = HTTPServer(('', 80), WordsHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,python-3.x |>
<| c |>
Thanks so much! I 