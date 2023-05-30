#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word1> <word2> ..." % sys.argv[0])
        sys.exit()
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    
    if len(sys.argv) > 3:
        for i in range(3, len(sys.argv)):
            word1 += " " + sys.argv[i]
    
    if len(sys.argv) > 4:
        for i in range(4, len(sys.argv)):
            word2 += " " + sys.argv[i]
    
    word1 = word1.strip()
    word2 = word2.strip()
    
    words = []
    
    for word in word1.split():
        words.append(word)
    
    for word in word2.split():
        words.append(word)
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    
    for word in words:
        sys.stdout.write("<hr>%s<hr>" % word)
    
    sys.stdout.write("</body></html>")
    
    sys.stdout.flush()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
