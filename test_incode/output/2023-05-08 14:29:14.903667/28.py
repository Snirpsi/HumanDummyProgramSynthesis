#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that enumerates a list of words.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse
    from urllib.request import urlopen

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = self.path.split("?")
            path = parsed[0]
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(words, "utf8"))
            else:
                words = path.split("/")
                word = words[-1]
                index = words.index("index")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                word = words[index]
                index = words.index("count")
                word = words[index]
                index = words.index("words")
                word = words[index]
                index = words.index("word")
                

