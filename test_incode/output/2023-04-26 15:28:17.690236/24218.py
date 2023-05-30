#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordfile>" % sys.argv[0])
        sys.exit()
    
    wordfile = sys.argv[1]
    
    words = []
    
    with open(wordfile, 'r') as wordfile:
        for line in wordfile:
            words.append(line.strip())
    
    words.sort()
    
    wordlist = " ".join(words)
    
    wordlist = wordlist.replace(' ', '%20')
    
    print("<html><head>")
    print("<title>Wordlist</title>")
    print("</head><body>")
    print("<h1>Wordlist</h1>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(wordlist))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>")
    print("<p>")
    print("Wordlist contains %d words. " % len(words))
    print("</p>