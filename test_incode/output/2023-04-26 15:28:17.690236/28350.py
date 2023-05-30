#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    # Open the file words.txt
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Open the file index.html
    with open('index.html', 'w') as f:
        f.write('<html><head><title>Words</title></head>')
        f.write('<body>')
        f.write('<table>')
        f.write('<tr><th>Word</th><th>Frequency</th></tr>')
        
        # Loop over all words in the file
        for word in words:
            f.write('<tr><td>{}</td><td>{}</td></tr>'.format(word, 