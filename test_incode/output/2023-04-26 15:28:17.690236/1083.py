#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = [int(i) for i in sys.argv[1:]]
    httpd = make_server('', ports[0], Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,port,flask |>
<| c |>
This doesn't work for me. I'm getting `NameError: name 'ports' is not defined` when I try running this code.
<|/ c |>
<| c |>
I ran this on my local machine and it worked fine. Are you sure you are running this script from the same directory as your flask app?
<|/ c |>
<| c |>
Yes, I'm running it from the same directory. I also tried running it from the same directory as my flask app but got the same error.
<|/ c |>
<| c |>
I ran it from the same directory as my flask app and it worked fine. Are you sure you are running this script from the same directory as your flask app?
<|/ c |>
<| c |>
Yes, I'm running it from the same directory as my flask app. I even tried running it from the same directory as my flask app but got the same error.
<|/ c |>
<| a tags=python,webserver,port,flask |>
I ran into the same problem and found a solution that worked for me:
<code>
if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
</code>
<|/ a dscore=0 |>