#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    #It serves up an html file that displays the words in a table.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import cgi
    import os
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '<html>'
            html += '<head><title>Word List</title></head>'
            html += '<body>'
            html += '<table>'
            html += '<tr><th>Word</th><th>Count</th></tr>'
            for word in words:
                html += '<tr><td>%s</td><td>%s</td></tr>' % (word, word.count(word))
            html += '</table>'
            html += '</body>'
            html += '</html>'
            self.wfile.write(bytes(html, 'utf-8'))
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

