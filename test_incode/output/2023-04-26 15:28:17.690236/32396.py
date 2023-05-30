#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or calculates a list of words. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that enumerates all ports or calculates a list of words.')
    parser.add_argument('-p', '--port', type=int, default=8080,
                        help='The port to listen on (default: %(default)s)')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all available words')
    args = parser.parse_args()
    
    # Start webserver
    webserver(args.port, args.list)
    
