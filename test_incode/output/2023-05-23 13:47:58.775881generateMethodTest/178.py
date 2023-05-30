#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that opens a http request.
    server = HTTPServer(('', 80), RequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your answer. I've tried your code, but I still get the same error. I've edited my question to include the full code. Can you please take a look?
<|/ c |>
<| c |>
I've edited my answer to include a full working example. Try it out and let me know if it works.
<|/ c |>
<| c |>
Thanks for your help. I've tried your code, but I still get the same error. I've edited my question to include the full code. Can you please take a look?
<|/ c |>
<| c |>
I've edited my answer to include a full working example. Try it out and let me know if it works.
<|/ c |>
<| c |>
Thanks for your help. I've tried your code, but I still get the same error. I've edited my question to include the full code. Can you please take a look?
<|/ c |>
<| a dscore=0 |>
I finally found the solution. 
I needed to add the following line to my code:
<code>
server.socket = ssl.wrap_socket(server.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
</code>
<|/ a tags=python,ssl,sockets |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a tags=python,ssl,sockets |>
<| a tags=python,ssl,sockets |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgraded to python 3.6 and it worked.
<|/ a dscore=0 |>
<| a dscore=0 |>
I ran into this problem and found that my problem was that I was using an old version of python 2.7. 
I upgra