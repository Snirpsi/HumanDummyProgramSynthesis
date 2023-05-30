#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that enumerates a http request.
    def enumerate_request(request):
        request = requests.get(url)
        request.raise_for_status()
        return request

    #A function that parses the response and prints it.
    def print_response(response):
        print(response.text)

    #A function that enumerates all the requests and prints them.
    requests = enumerate_request(url)
    for request in requests:
        print_response(request)

