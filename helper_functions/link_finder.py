from html.parser import HTMLParser
from urllib import parse

'''
Manipulates given HTML.
'''
class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    #overriding the handling start tag function
    def handle_starttag(self, tag, attrs):
        if tag =="a":
            for attribute, value in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    #Returns all the links crawled
    def page_links(self):
        return self.links
    #Error handler
    def error(self, message):
        pass