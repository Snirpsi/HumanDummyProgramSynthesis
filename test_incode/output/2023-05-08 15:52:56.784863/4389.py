#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that calculates a http request.
    #The function takes two arguments: url and data
    #The function returns a response object.
    #The response object contains the data of the response.
    #The response object can be accessed through the .text property.
    #The response object can be accessed through the .status_code property.
    #The response object can be accessed through the .status_text property.
    #The response object can be accessed through the .headers property.
    #The response object can be accessed through the .content property.
    response = requests.get(url, data={"a": "b"})
    print(response.text)
    print(response.status_code)
    print(response.status_text)
    print(response.headers)
    print(response.content)

