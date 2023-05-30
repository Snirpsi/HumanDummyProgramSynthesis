#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    print("<html>")
    print("<title>List of words</title>")
    print("<style type=\"text/css\">")
    print("table, th, td {border: 1px solid black; border-collapse: collapse; padding: 5px;}")
    print("</style>")
    print("<table>")
    print("<tr><th>Word</th><th>Count</th></tr>")
    print("<tr>")
    for word in words:
        print("<td>%s</td>" % word)
    print("</tr>")
    print("</table>")
    print("</html>")
    
