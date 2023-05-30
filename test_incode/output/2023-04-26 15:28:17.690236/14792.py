#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import json

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request """
            params = parse_qs(urlparse(self.path).query)
            numbers = params.get('numbers')
            if numbers is None:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No numbers given'}))
                return
            numbers = numbers.split(',')
            for number in numbers:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({'number': number}))
                return

    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()
</code>
<|/ a tags=python,flask,html,python-3.x |>
<| c |>
Thanks for your answer. I'm going to try this and let you know how it goes.
<|/ c |>
<| c |>
It worked! Thanks a lot! I didn't know that you could use 'GET' as a method in the url parameters. I thought it was only for POST and PUT requests. Thanks again!
<|/ c |>
<| c |>
No problem! Glad I could help.
<|/ c |>
<| c |>
