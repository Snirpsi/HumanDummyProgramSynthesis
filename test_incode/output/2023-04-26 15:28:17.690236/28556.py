#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Write words to stdout
    for line in words:
        print(line)
    
    # Print the length of each word
    lengths = []
    for word in words:
        lengths.append(len(word))
    
    # Print the average length of each word
    averages = []
    for word in words:
        averages.append(sum(lengths)/len(lengths))
    
    # Print the average length of each word with spaces
    averages_spaced = []
    for word in words:
        averages_spaced.append(" ".join(map(str, averages)))
    
    # Print the average length of each word with tabs
    averages_tab = []
    for word in words:
        averages_tab.append(" ".join(map(str, averages)))
    
    # Print the average length of each word with spaces
    averages_spaced_tab = []
    for word in words:
        averages_spaced_tab.append(" ".join(map(str, averages)))
    
    # Print the average length of each word with tabs
    averages_tab