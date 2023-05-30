#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that prints fruits.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            fruits = query["fruits"]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                '<html><head><title>Fruits</title></head>'
                '<body>'
                '<table>'
                '<tr><th>Fruit</th><th>Count</th></tr>'
                '<tr><td>{}</td><td>{}</td></tr>'
                '</table>'
                '</body></html>'.format(fruits,len(fruits)), 'utf-8'))

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()
</code>
<|/ a tags=python,html,python-3.x |>
<| c |>
Thanks for your answer. I'm going to try it out and see how it goes.
<|/ c |>
<| c |>
It works perfectly! Thank you so much!
<|/ c |>
<| c |>
You're welcome! If this answer solved your problem, please consider accepting it by clicking the checkmark to the left of the answer.
<|/ c |>
<| c |>
I did that, but I still have to wait 2 days to accept the answer. Thanks again!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a |>
<code>
#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
cgitb.enable()
import cgi
import cgitb
c