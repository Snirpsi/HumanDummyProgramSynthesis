#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class CalculatorHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = []
            
            ports.append(8080)
            ports.append(8000)
            
            for port in ports:
                
                calculator = Calculator()
                
                calculator.calculate(port)
                
                self.wfile.write(calculator.calculated_data)
                
    server = HTTPServer(('', 8080), CalculatorHandler)
    
    print('Serving on port 8080')
    
    server.serve_forever()
    
