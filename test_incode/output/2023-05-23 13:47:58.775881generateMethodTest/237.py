#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that converts ports.
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. Unfortunately this does not work for me. I am not able to access my webserver from my local machine.
<|/ c |>
<| c |>
I added a working example to my answer. Hopefully that helps.
<|/ c |>
<| c |>
Thanks for your answer. I tried your example but I am still not able to access my webserver from my local machine. I added my code to the original post.
<|/ c |>
<| c |>
I added a working example to my answer. Hopefully that helps.
<|/ c |>
<| c |>
Thanks for your answer. I tried your example but I am still not able to access my webserver from my local machine. I added my code to the original post.
<|/ c |>
<| a tags=python,httpserver,python-3.x,webserver |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a dscore=1 |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a tags=python,httpserver,python-3.x,webserver |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a tags=python,httpserver,python-3.x,webserver |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a dscore=0 |>
<| a tags=python,httpserver,python-3.x,webserver |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>
<| a tags=python,httpserver,python-3.x,webserver |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
I solved my problem by adding this line to my code:
<code>
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,httpserver,python-3.x,webserver |>