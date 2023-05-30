#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    import math

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request handler. """
            path = urlparse(self.path).path
            query = parse_qs(urlparse(self.path).query)
            
            if path == '/':
                """ Display a welcome message and quit. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>Welcome to my server!</h1>')
                return
            
            if path == '/multiply':
                """ Handle the GET request to /multiply. """
                words = []
                
                for word in query:
                    words.append(word)
                
                words = list(set(words))
                
                """ Get the length of the list. """
                length = len(words)
                
                """ Get the sum of the list. """
                sum = 0
                
                for word in words:
                    sum += word
                
                """ Get the product of the list. """
                product = 1
                
                for word in words:
                    product *= word
                
                """ Get the average of the list. """
                average = sum / length
                
                """ Get the standard deviation of the list. """
                standard_deviation = math.sqrt(sum / length - (sum / length) ** 2)
                
                """ Get the standard deviation of the list. """
                variance = standard_deviation / math.sqrt(length)
                
                """ Get the standard deviation of the list. """
                mode = math.fmode(words)
                
                """ Get the standard deviation of the list. """
                mode = mode[0]
                
                """ Get the standard deviation of the list. """
                mode = math.fmean(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmedian(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmin(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmax(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fsum(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fvar(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fstd(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fvar(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmean(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmedian(words)
                
                """ Get the standard deviation of the list. """
                mode = math.fmin(words)
                
                """ Get the standard deviation of the list. """