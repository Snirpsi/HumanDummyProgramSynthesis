#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports or removes words. """    
    while True:
        words = input("Enter a word: ")
        if words:
            words = words.split()
            for word in words:
                word = word.strip()
                if word not in ports:
                    ports.append(word)
        else:
            break
    print(ports)
</code>
<|/ a dscore=0 tags=python |>
<| c |>
This works perfectly for me. Thank you so much!
<|/ c |>
<| c |>
Glad to help!
<|/ c |>
<| a tags=python |>
<code>
def ports_list(ports):
    ports_list = []
    for port in ports:
        ports_list.extend(port.split(' '))
    return ports_list
</code>
<|/ a dscore=0 |>
<| c |>
This works perfectly for me. Thank you so much!
<|/ c |>
<| a |>
<code>
def ports_list(ports):
    ports_list = []
    for port in ports:
        ports_list.extend(port.split(' '))
    return ports_list
</code>
<|/ a dscore=0 tags=python |>