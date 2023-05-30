#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or calculates a list of numbers. """    
    
    # Parse command line arguments
    opts, args = getopt.getopt(sys.argv[1:], '', ['help'])
    
    # Print help message if needed
    if opts.count('help'):
        print('Usage: python webserver.py [options]')
        print('Options:')
        print('  -h, --help  Print this help message and exit.')
        sys.exit(0)
    
    # Print help message if needed
    if opts.count('-h'):
        print('Usage: python webserver.py [options]')
        print('Options:')
        print('  -h, --help  Print this help message and exit.')
        sys.exit(0)
    
    # Parse command line arguments
    port = int(args[0])
    
    # Start server
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    # Start server
    