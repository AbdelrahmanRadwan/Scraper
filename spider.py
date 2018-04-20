from urllib.request import urlopen
from link_finder import LinkFinder
from helper import *
'''
Grasp all the HTML from a page.
'''
class spider:

    # Class variable (shared var between all the spiders)
    project_name = ""
    base_url = ""
    domain_name = ""
    crawled_file = ""
    queue_file = ""
    queue = set() # the waiting list
    crawled = set() # the crawled pages

    #If it's the first spider crawling the first home page...
    @staticmethod
    def boot():
        create_project_dir(directory=spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    def crawl_page(self):
        pass

    def __int__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.domain_name = domain_name
        spider.base_url = base_url
        spider.queue_file = spider.project_name + "/queue.txt"
        spider.crawled_file = spider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("First spider", spider.base_url)
