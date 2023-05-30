#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, print_input)
    httpd.serve_forever()
</code>
<|/ a tags=python,flask |>
<| a |>
<code>
from flask import Flask, render_template, request
app = Flask(__name__).route('/')
def hello_world():
    return render_template('index.html')
</code>
<|/ a dscore=0 tags=python,flask |>