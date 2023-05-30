#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        numbers = sys.argv[1:]
    else:
        numbers = range(1,10)
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    numbers_str = ""
    words_str = ""
    
    for number in numbers:
        numbers_str += str(number) + " "
    
    for word in words:
        words_str += word + " "
    
    print("Content-type: text/html")
    print("<html>")
    print("<body>")
    print("<table>")
    print("<tr>")
    print("<th>Numbers</th>")
    print("<th>Words</th>")
    print("</tr>")
    
    for number in numbers:
        print("<tr>")
        print("<td>" + str(number) + "</td>")
        print("<td>" + words_str + "</td>")
        print("</tr>")
    
    print("</table>")
    print("</body>")
    print("</html>")
    
