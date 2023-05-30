#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or adds user input. """    
    while True:
        port = int(input("Enter a port number: "))
        if port < 0 or port > 65535:
            print("Invalid port number")
        else:
            break
    print("The port number is", port)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! This was very helpful.
<|/ c |>
<| c |>
Glad it helped!
<|/ c |>
<| c |>
