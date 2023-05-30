#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import cgi
    import json
    import math

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            number = query['number']
            numbers.append(number)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json.dump({'numbers': numbers}, indent=2)

    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()

    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import 