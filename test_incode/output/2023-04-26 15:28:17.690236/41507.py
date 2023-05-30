#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by adding words to the list. """
            
            # Get the list of words from the GET request
            words = self.path.split('=')[1]
            
            # Add each word from the GET request to the list
            for word in words.split(','):
                words.append(word)
            
            # Send the list back to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(