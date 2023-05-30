#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or enumerates numbers. """    
    
    # Parse command line arguments
    args = parse_args()
    
    # Start server
    server = Server(args.host, args.port)
    server.serve()
    
