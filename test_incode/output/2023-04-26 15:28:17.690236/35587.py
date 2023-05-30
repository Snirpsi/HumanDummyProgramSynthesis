#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or converts a list of numbers. """    
    import sys
    from getopt import getopt, GetoptError
    import socketserver
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from wordlist import WordList
    from wordlist import WordListError
    
    usage = "usage: wordlist.py [-h] [-p port] [-c count] [-d dir] [-n num] [-l lang] [-s server] [-t type] [-u url]"
    
    try:
        opts, args = getopt(sys.argv[1:], 'hp:c:d:n:l:s:t:u:', [
            'help', 'port=', 'count=', 'dir=', 'num=', 'lang=', 'server=', 'type=', 'url=',
        ])
    except GetoptError:
        print(usage)
        sys.exit(2)
    
    port = 0
    count = 1
    dir = ''
    num = 0
    lang = ''
    server = ''
    type = ''
    url = ''
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(usage)
            sys.exit()
        elif opt in ('-p', '--port'):
            try:
                port = int(arg)
            except ValueError:
                print(usage)
                sys.exit(2)
        elif opt in ('-c', '--count'):
            try:
                count = int(arg)
            except ValueError:
                print(usage)
                sys.exit(2)
        elif opt in ('-d', '--dir'):
            dir = arg
        elif opt in ('-n', '--num'):
            num = int(arg)
        elif opt in ('-l', '--lang'):
            lang = arg
        elif opt in ('-s', '--server'):
            server = arg
        elif opt in ('-t', '--type'):
            type = arg
        elif opt in ('-u', '--url'):
            url = arg
    
    wordlist = WordList(dir, num, lang, type, server, url)
    
    handler = WordListHandler(wordlist)
    httpd = HTTPServer(('', port), handler)
    
    print("Serving at port %d..." % port)
    httpd.serve_forever()
    
