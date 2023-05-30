#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    #It returns a response object.
    #It also prints the response code.
    response = requests.get(url)
    print(response.status_code)
    print(response.text)

