#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or adds numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import StringIO
    import json
    
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handles GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Root page. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                """ Get a list of words. """
                
                words = []
                
                for word in words:
                    words.append(word)
                    
                """ Get a number from user. """
                
                number = int(input('Enter a number: '))
                
                """ Convert the number to a word. """
                
                word = number%10
                
                """ Print the word and number. """
                
                print('The word is ' + word + ' and the number is ' + str(number))
                
            elif parsed_url.path == '/words':
                """ Get a list of words. """
                
                words = []
                
                for word in words:
                    words.append(word)
                    
                """ Print the list of words. """
                
                print(json.dumps(words))
                
            elif parsed_url.path == '/numbers':
                """ Get a list of numbers. """
                
                numbers = []
                
                for number in numbers:
                    numbers.append(number)
                    
                """ Print the list of numbers. """
                
                print(json.dumps(numbers))
                
            else:
                """ Invalid path. """
                
                self.send_response(404)
                self.end_headers()
                
    
    
    server_address = ('', 8080)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving on port 8080...')
    
    httpd.serve_forever()
    
