#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that iterates over user input.
    
    #The port to listen on
    port = int(sys.argv[1])
    
    #The webserver will listen on port 80
    server = HTTPServer(("", port), MyHandler)
    
    #Start the webserver
    server.serve_forever()

