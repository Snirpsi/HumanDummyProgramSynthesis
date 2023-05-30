#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    #It returns a string with the response.
    #The response is decoded using utf-8.
    #The response is sent to the standard output stream.
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    response_str = response.read().decode("utf-8")
    print(response_str)
    #The response is sent to the standard error stream.
    error_stream = sys.stderr
    error_stream.write(response_str)
    error_stream.flush()
    #The request is closed.
    request.close()

