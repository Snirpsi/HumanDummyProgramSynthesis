#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and removes all ports. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that returns user input and removes all ports.')
    parser.add_argument('port', metavar='PORT', type=int, help='port to listen on')
    args = parser.parse_args()
    
    # Start server
    httpd = make_server(args.port, handle_request, 