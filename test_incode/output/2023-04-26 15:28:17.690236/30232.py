#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s [words.txt]" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    server_address = ('', 8000)
    
    httpd = HTTPServer(server_address, WordsHandler)
    
    httpd.serve_forever()

<|/ file filename=words.py source=github |>