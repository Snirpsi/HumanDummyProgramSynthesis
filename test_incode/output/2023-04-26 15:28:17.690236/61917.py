#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or enumerates numbers. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that converts user input or enumerates numbers')
    parser.add_argument('numbers', metavar='N', type=int, nargs='+', help='a number or list of numbers to enumerate')
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    parser.add_argument('-v', '--verbose', action='store_true', help='print debug information')
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    # Start server
    server = HTTPServer(("", args.port), SimpleHTTPRequestHandler)
    
    # Start server
    server.serve_forever()
