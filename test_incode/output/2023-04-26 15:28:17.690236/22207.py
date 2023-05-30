#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that multiplies a list of words. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            query = parse_qs(urlparse(self.path).query)
            
            if query['op'] == 'add':
                words = self.path.split('/')
                
                word1 = words[0]
                word2 = words[1]
                
                word1 = word1.strip()
                word2 = word2.strip()
                
                word1 = word1.upper()
                word2 = word2.upper()
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = [w.upper() for w in word1]
                word2 = [w.upper() for w in word2]
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
                word2 = word2.split()
                
                word1 = ' '.join(word1)
                word2 = ' '.join(word2)
                
                word1 = word1.split()
