#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that stores a http request.
    def http_request_handler(request):
        request.urlretrieve(url, "./" + request.url.split("/")[-1])
    
    #A function that prints the response of the http request.
    def http_response_handler(response):
        print(response.read())
    
    #A function that prints the response of the http request.
    def http_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_response_handler(response):
        print(response.read())
    
    #A function that prints the response of the http request.
    def https_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_connection_ssl_connection_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_connection_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_connection_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def https_proxy_connection_ssl_connection_ssl_error_handler(error):
        print(error)
    
    #A function that prints the response of the http request.
    def http_proxy_connection_ssl_connection_ssl_connection_ssl_handler(request):
        print(request.url)
    
    #A function that prints the response of the http request.
    def 

