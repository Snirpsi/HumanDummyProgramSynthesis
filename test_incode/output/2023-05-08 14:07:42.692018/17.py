#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A minimal webserver that enumerates a http request.
    server = HTTPServer(('', 80), RequestHandler)
    server.serve_forever()
</code>
<|/ a dscore=0 |>
<| c |>
Thanks very much for your help. I 