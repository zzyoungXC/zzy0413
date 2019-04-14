html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')

#print(soup.prettify())

for a in soup.find_all('a'):
    print(a['href'])

#soup.find_all('a')

class UrlPrase(object):
    def __init__(self):
        self.new_url = set()
        self.new_img = set()

    def __get_url(self,base:str,soup:BeautifulSoup):
        for a in  soup.find_all('a'):
            href=a['href']
            target_url=urljoin(base,href)
            self.new_url.add(target_url)

    def __get_url(self, base: str, soup: BeautifulSoup):
        for a in soup.find_all('img'):
            src = a['src']
            target_img = urljoin(base, href)
            self.new_img.add(target_img)

    def __get_img(self, base: str, soup: BeautifulSoup):
        pass

    def html_parse(self,base,html_doc):
        soup=BeautifulSoup(html_doc,'html.parser')
        self.__get_url(base,soup)
        self.__get_img(base,soup)
        return self.new_url,self.new_img