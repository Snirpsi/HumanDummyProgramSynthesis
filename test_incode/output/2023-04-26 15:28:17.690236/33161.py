#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    
    httpd = HTTPServer(("", 8080), RequestHandler)
    httpd.serve_forever()
    
    ports.append(8080)
    
    httpd = HTTPServer(("", 80), RequestHandler)
    httpd.serve_forever()
    
    ports.append(80)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), RequestHandler)
    httpd.serve_forever()
    
    ports.append(443)
    
    httpd = HTTPServer(("", 443), Request