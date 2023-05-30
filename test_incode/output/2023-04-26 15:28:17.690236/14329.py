#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port or converts words. """    
    import sys
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8080, MyApp)
    httpd.serve_forever()
</code>
<|/ a tags=python,wsgiref,python-3.x dscore=0 |>
<| c |>
Thanks for your answer. Unfortunately this does not solve my problem. I'm still getting `404 Not Found` errors. My application is running on port 80 and I'm accessing it via `http://localhost/myapp`
<|/ c |>
<| c |>
It works fine for me. Are you sure the port is correct? Can you try `http://localhost/myapp` ?
<|/ c |>
<| c |>
Yes, I'm sure. I've also tried `http://localhost/myapp:8080` but that does not work either
<|/ c |>
<| c |>
I've just tried it again. Works fine for me. Are you sure the port is correct? Can you try `http://localhost/myapp` ?
<|/ c |>
<| c |>
Yes, I'm sure. I've also tried `http://localhost/myapp:8080` but that does not work either
<|/ c |>
<| a |>
I solved it by changing the port to 8080 instead of 80. Thanks for your help!
<|/ a dscore=0 tags=python,wsgiref,python-3.x |>
<| c |>
This does not provide an answer to the question. To critique or request clarification from an author, leave a comment below their post.
<|/ c |>