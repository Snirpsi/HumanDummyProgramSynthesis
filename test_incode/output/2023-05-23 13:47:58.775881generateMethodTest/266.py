#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    #This example is intended to be run from the command line with 
    #the command "python -m http.server"
    import http.server
    import socketserver
    import argparse
    import sys
    
    #Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that returns user input.')
    parser.add_argument('-p', '--port', type=int, default=8000, help='port to listen on')
    parser.add_argument('-u', '--user', type=str, help='user to log in')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()
    
    #Set up logging
    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    #Set up port and user variables
    port = args.port
    user = args.user
    
    #Set up socket server
    class SocketHandler(socketserver.BaseRequestHandler):
        #Handle requests from clients
        def handle(self):
            #Get user input
            user_input = self.request.recv(1024).strip()
            
            #Log user input
            print('User: ' + user_input)
            
            #Send response to client
            self.request.sendall('User input received.')
            
            #Close connection
            self.request.close()
    
    #Create server
    server = socketserver.TCPServer(('localhost', port), SocketHandler)
    
    #Start server
    server.serve_forever()
    
    #Close server
    server.socket.close()
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server
    
    #Run server