#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words and adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordlist>" % sys.argv[0])
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = []
    
    with open(wordlist) as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    wordlist = " ".join(words)
    
    print("<html><head><title>Wordlist</title></head><body>")
    print("<table>")
    print("<tr><th>Word</th><th>Count</th></tr>")
    
    for word in words:
        print("<tr><td>%s</td><td>%s</td></tr>" % (word, len(words)))
    
    print("</table>")
    
    print("</body></html>")
    
    
