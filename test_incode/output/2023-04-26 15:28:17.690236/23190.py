#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that removes user input.')
    parser.add_argument('-p', '--port', type=int, default=8000, help='The port to listen on.')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode.')
    parser.add_argument('user', type=str, help='The user to remove.')
    args = parser.parse_args()
    
    # Start webserver
    webserver.run(args.port, args.debug, args.user)

<|/ file ext=.py |>