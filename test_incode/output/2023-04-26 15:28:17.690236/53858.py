#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or prints a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import math
    
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple handler for handling HTTP requests. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            q = parse_qs(urlparse(self.path).query)
            
            
            if q['op'] == 'mult':
                
                num1 = float(q['num1'])
                num2 = float(q['num2'])
                
                
                num3 = num1 * num2
                
                
                num4 = num1 * num3
                
                
                num5 = num1 * num4
                
                
                num6 = num1 * num5
                
                
                num7 = num1 * num6
                
                
                num8 = num1 * num7
                
                
                num9 = num1 * num8
                
                
                num10 = num1 * num9
                
                
                num11 = num1 * num10
                
                
                num12 = num1 * num11
                
                
                num13 = num1 * num12
                
                
                num14 = num1 * num13
                
                
                num15 = num1 * num14
                
                
                num16 = num1 * num15
                
                
                num17 = num1 * num16
                
                
                num18 = num1 * num17
                
                
                num19 = num1 * num18
                
                
                num20 = num1 * num19
                
                
                num21 = num1 * num20
                
                
                num22 = num1 * num21
                
                
                num23 = num1 * num22
                
                
                num24 = num1 * num23
                
                
                num25 = num1 * num24
                
                
                num26 = num1 * num25
                
                
                num27 = num1 * num26
                
                
                num28 = num1 * num27
                
                
                num29 = num1 * num28
                
                
                num30 = num1 * num29
                
                
                num31 = num1 * num30
                
                
                num32 = num1 * num31
                
                
                num33 = num1 * num32
                
                
                num34 = num1 * num33
                
