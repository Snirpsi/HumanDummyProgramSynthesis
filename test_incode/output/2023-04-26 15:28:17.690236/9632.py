#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or iterates over numbers. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that converts user input or iterates over numbers')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-p', '--port', type=int, default=8000, help='Port number to listen on')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('-f', '--force', action='store_true', help='Force a restart without user input')
    parser.add_argument('user', type=str)
    args = parser.parse_args()
    
    # Start webserver
    webserver.run(args.port, args.interactive, args.force, args.user)
    
