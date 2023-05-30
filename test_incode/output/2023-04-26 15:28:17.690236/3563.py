#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that stores user input.')
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port number')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    # Start server
    server = HTTPServer(('', args.port), SimpleHTTPRequestHandler)
    
    # Enable debug mode
    if args.debug:
        server.