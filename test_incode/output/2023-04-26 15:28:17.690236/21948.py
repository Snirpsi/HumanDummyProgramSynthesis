#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that adds user input.')
    parser.add_argument('user', metavar='user', type=str, help='The name of the user to add.')
    parser.add_argument('-p', '--port', type=int, default=8000, metavar='port', help='The port to listen on.')
    args = parser.parse_args()
    
    # Start webserver
    server = HTTPServer(('', args.port), UserInputHandler)
    server.serve_forever()
    
