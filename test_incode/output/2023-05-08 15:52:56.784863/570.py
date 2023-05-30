#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that iterates over a http request.
    #The function returns one line at a time.
    #The function reads the response from the server.
    #The function prints the line to the console.
    for line in iter(lambda: requests.get(url, stream=True).text, ""):
        print(line)

