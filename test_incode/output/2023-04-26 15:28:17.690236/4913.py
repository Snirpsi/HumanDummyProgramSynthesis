#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    import socket
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            words = self.path.split('/')
            
            if len(words) != 2:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid number of arguments.")
                return
            
            word1 = words[0]
            word2 = words[1]
            
            word1 = word1.upper()
            word2 = word2.upper()
            
            word1 = word1.strip()
            word2 = word2.strip()
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = word1.split()
            word2 = word2.split()
            
            word1 = [word.lower() for word in word1]
            word2 = [word.lower() for word in word2]
            
            word1 = ' '.join(word1)
            word2 = ' '.join(word2)
            
            word1 = 