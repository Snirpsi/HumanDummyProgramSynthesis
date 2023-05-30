#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    from multiprocessing import Process
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            args = parse_qs(
                self.path.split('?')[1],
                keep_blank_values=True,
                strict_parsing=True
            )
            
            numbers = args.get('numbers', [])
            
            if len(numbers) == 0:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad request')
                return
            
            numbers = [int(x) for x in numbers]
            
            proc = Process(target=multiply, args=(numbers,))
            proc.start()
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
            
    httpd = BaseHTTPRequestHandler()
    httpd.