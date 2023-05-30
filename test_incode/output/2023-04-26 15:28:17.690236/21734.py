#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or adds user input. """    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that converts user input or adds user input.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-p', '--port', default=8000, type=int, help='port to listen on')
    parser.add_argument('-d', '--directory', default='.', help='directory to serve static files from')
    parser.add_argument('-c', '--config', default='config.ini', help='configuration file')
    parser.add_argument('-l', '--log-file', default='log.txt', help='log file to write to')
    parser.add_argument('-i', '--ignore', default='.gitignore', help='ignore files')
    parser.add_argument('-f', '--force', default=False, action='store_true', help='force reloading config file')
    args = parser.parse_args()
    
    # Load configuration file
    config = ConfigParser.ConfigParser()
    config.read(args.config)
    
    # Load ignore file
    ignore = set(config.items('ignore'))
    
    # Load log file
    log_file = open(args.log_file, 'a')
    
    # Load directory to serve static files from
    directory = args.directory
    
    # Start server
    server = HTTPServer(('', args.port), SimpleHTTPRequestHandler)
    
    # Start logging
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    
    # Start server
    server.serve_forever()
    
    # Stop server
    server.socket.close()
    
    # Stop logging
    logging.shutdown()
    logging.