#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    import socketserver
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs
    from wordlist import WordList

    class WordListHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request with words. """
            parsed_url = urlparse(self.path)
            words = WordList()
            words.load_words(parsed_url.path)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(words.to_json())

    httpd = socketserver.TCPServer(("", 8000), WordListHandler)
    httpd.serve_forever()
