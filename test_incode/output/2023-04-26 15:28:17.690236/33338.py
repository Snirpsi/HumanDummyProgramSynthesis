#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    ports = [int(p) for p in sys.argv[1:]]
    server = HTTPServer(("", ports[0]), Handler)
    server.serve_forever()
</code>
<|/ a tags=python,sockets,webserver |>
<| c |>
Thanks for your answer. I'm new to python and I didn't know that you can do that. I'll try it out and see how it goes.
<|/ c |>
<| c |>
