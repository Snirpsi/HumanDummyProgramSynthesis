#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Remove user input.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug output.')
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port number.')
    parser.add_argument('user', type=str, help='User to remove.')
    args = parser.parse_args()
    
    # Print debug output
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    
    # Print verbose output
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    
    # Start webserver
    server = HTTPServer(('', args.port), RemoveUserInputHandler)
    
    # Start webserver
    server.serve_forever()

<|/ file ext=.py source=github |>