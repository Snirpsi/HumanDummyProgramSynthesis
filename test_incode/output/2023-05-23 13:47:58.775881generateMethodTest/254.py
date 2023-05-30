#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that iterates over all ports.
    httpd = HTTPServer(("", ports[0]), Handler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. Unfortunately I cannot use your solution, because I do not have access to the server's code. My server is running on a remote server and I cannot install any additional packages on that server. Also, I cannot install any additional packages on my local machine.
<|/ c |>
<| c |>
I added a python script to my answer. Hope it helps.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately I cannot use your solution, because I do not have access to the server's code. My server is running on a remote server and I cannot install any additional packages on that server. Also, I cannot install any additional packages on my local machine.
<|/ c |>
<| c |>
I added a python script to my answer. Hope it helps.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately I cannot use your solution, because I do not have access to the server's code. My server is running on a remote server and I cannot install any additional packages on that server. Also, I cannot install any additional packages on my local machine.
<|/ c |>
<| a dscore=1 |>
I finally found a solution that works for me. 
I used the solution proposed by Kevin Burr to install a python script that iterates over all available ports and prints out the available ports. 
I used the following command:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to start my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to stop my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Stopping HTTPServer ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>
I then used the following command to restart my server:
<code>
python -m http.server
</code>
The output looks like this:
<code>
Serving HTTP on 0.0.0.0 port 8000 ...
</code>