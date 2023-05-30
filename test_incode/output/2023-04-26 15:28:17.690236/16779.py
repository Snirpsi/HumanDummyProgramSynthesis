#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from io import StringIO

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            query_dict = parse_qs(parsed_url.query)
            
            if parsed_url.path == '/':
                """ Display a welcome message. """
                send_response(200)
                send_header('Content-type', 'text/html')
                send_header('Content-length', '0')
                end_headers()
                
                """ Send the HTML content. """
                content = """
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
                """
                
                """ Send the content. """
                self.wfile.write(content.encode('utf-8'))
            else:
                """ Handle the request. """
                
                """ Get the word list from the query string. """
                word_list = query_dict.get('words')
                
                """ Convert the word list to a list. """
                word_list = word_list.split(',')
                
                """ Multiply the word list by 3. """
                word_list = list(map(int, word_list))
                
                """ Send the result. """
                send_response(200)
                send_header('Content-type', 'text/html')
                send_header('Content-length', str(len(word_list)))
                end_headers()
                
                """ Send the HTML content. """
                content = """
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
</html>
                """
                
                """ Send the content. """
                self.wfile.write(content.encode('utf-8'))
                
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
