#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            q = parse_qs(urlparse(self.path).query)
            numbers = q['numbers']
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers)

    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()

<|/ file ext=.py source=github |>
#!/usr/bin/env python
#
# Simple HTTP server that adds numbers to the page.
#
# Usage: python add_numbers.py [numbers]
#
# Numbers can be passed as query parameters or as POST data.
#
# Example:
#   python add_numbers.py numbers=1&numbers=2&numbers=3
#
# To use POST data, append a & to the end of the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3
#
# To use query parameters, append a ? to the end of the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3
#
# To use both query and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10&numbers=11
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10&numbers=11&numbers=12
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10&numbers=11&numbers=12&numbers=13
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10&numbers=11&numbers=12&numbers=13&numbers=14
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=4&numbers=5&numbers=6&numbers=7&numbers=8&numbers=9&numbers=10&numbers=11&numbers=12&numbers=13&numbers=14&numbers=15
#
# To use query parameters and POST data, append a & and a ? to the URL:
#   python add_numbers.py numbers=1&numbers=2&numbers=3&numbers=