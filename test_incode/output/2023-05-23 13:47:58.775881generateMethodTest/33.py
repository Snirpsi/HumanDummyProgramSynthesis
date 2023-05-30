#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that calculates all ports.
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()

    #A simple web page that displays the ports being used.
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            for port in ports:
                self.wfile.write(str(port))

    #Start the webserver
    httpd.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your reply. Unfortunately this does not work for me. I am running this on Ubuntu 16.04 LTS. I am also running Python 2.7.12. I am also running this on Windows 10. I am also running this on Windows 7. I am also running this on Windows 8.
<|/ c |>
<| c |>
I ran this on Ubuntu 16.04 LTS and Python 2.7.12 and it worked fine. Are you sure you ran it from the correct directory? Can you post the output of `which python` and `which python3`?
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| a dscore=0 |>
I ran this on Ubuntu 16.04 LTS and Python 2.7.12 and it worked fine. 
Are you sure you ran it from the correct directory? 
Can you post the output of: 
<code>
which python
which python3
</code>
<|/ a tags=python,python-2.7,python-3.x |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| a dscore=0 |>
I ran this on Ubuntu 16.04 LTS and Python 2.7.12 and it worked fine. 
Are you sure you ran it from the correct directory? 
Can you post the output of: 
<code>
which python
which python3
</code>
<|/ a tags=python,python-2.7,python-3.x |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python2.7 and /usr/bin/python3
<|/ c |>
<| c |>
I ran it from the directory where my python script is located. I am not sure what you mean by "the correct directory"? The output of `which python` and `which python3` are: /usr/bin/python