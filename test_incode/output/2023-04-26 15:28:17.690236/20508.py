#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    html = "<html>"
    html += "<head><title>Words</title></head>"
    html += "<body>"
    html += "<table>"
    html += "<tr><th>Word</th><th>Count</th></tr>"
    
    for word in words:
        html += "<tr><td>%s</td><td>%s</td></tr>" % (word, word.count(word))
    
    html += "</table>"
    html += "</body>"
    html += "</html>"
    
    sys.stdout.write(html)
    
