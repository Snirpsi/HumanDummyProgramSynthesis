#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #The first element in the list is the title of the page.
        title = soup.find('h1')
        
        #The second element in the list is the link to the page.
        link = soup.find('a')
        
        #The third element in the list is the content of the page.
        content = soup.find('div', class_='content')
        
        #The fourth element in the list is the date of the page.
        date = soup.find('div', class_='date')
        
        #The fifth element in the list is the author of the page.
        author = soup.find('div', class_='author')
        
        #The sixth element in the list is the summary of the page.
        summary = soup.find('div', class_='summary')
        
        #The seventh element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The eighth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The ninth element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The tenth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The eleventh element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The twelfth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The thirteenth element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The fourteenth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The fifteenth element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The sixteenth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The seventeenth element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The eighteenth element in the list is the tags of the page.
        tags = soup.find('div', class_='tags')
        
        #The ninteenth element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The twenty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The twenty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The thirty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The thirty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The fourty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The fourty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The fifty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The fifty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The sixty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The sixty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The seventy-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The seventy-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The eighty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The eighty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The ninety-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The ninety-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The twenty-first element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The twenty-second element in the list is the comments of the page.
        comments = soup.find('div', class_='comments')
        
        #The thirty-first element in the list is the comment

