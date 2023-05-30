#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
</code>
<|/ a dscore=1 |>
<| c |>
Thanks for your answer. I tried your solution, but I still get the same error. I also tried your second solution, but I still get the same error.
<|/ c |>
<| c |>
I added the full code of the python script to the question. Can you please have a look?
<|/ c |>
<| c |>
I added the full code of the python script to the question. Can you please have a look?
<|/ c |>
<| c |>
I added the full code of the python script to the question. Can you please have a look?
<|/ c |>
<| c |>
I added the full code of the python script to the question. Can you please have a look?
<|/ c |>
<| a tags=python,flask |>
I finally found a solution. 
I added the line 
<code>
app.run(host='0.0.0.0', port=8000)
</code>
to the file app.py and now it works.
<|/ a dscore=1 |>
<| c |>
This doesn't work for me on Flask 0.12.2
<|/ c |>
<| a tags=python,flask |>
I faced the same issue and found the solution by adding this line in the app.py file
<code>
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
</code>
<|/ a dscore=0 |>
<| a dscore=0 |>
I faced the same issue and found the solution by adding this line in the app.py file
<code>
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
</code>
<|/ a tags=python,flask |>