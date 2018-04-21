from urllib.request import urlopen

from helper_functions.link_finder import LinkFinder

from helper_functions.files_manager import *

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

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.domain_name = domain_name
        spider.base_url = base_url
        spider.queue_file = spider.project_name + "/queue.txt"
        spider.crawled_file = spider.project_name + "/crawled.txt"
        self.boot()
        self.crawl_page("First Spider", spider.base_url)

    #If it's the first spider crawling the first home page...
    @staticmethod
    def boot():
        create_project_dir(directory=spider.project_name)
        create_data_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file)
        spider.crawled = file_to_set(spider.crawled_file)

    #Add the crawled pages to the queue
    @staticmethod
    def add_links_to_queue(page_urls):
        for url in page_urls:
            if url not in spider.crawled and url not in spider.queue:
                if spider.base_url in url:
                    spider.queue.add(url)

    #Crawl all the pages in this url
    @staticmethod
    def gather_links(page_url):
        html_string = ""
        try:
            response = urlopen(page_url)
            if "text/html" in response.getheader("Content-Type"):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except:
            return ""
        return finder.page_links()

    @staticmethod
    def update_spider_file():
        set_to_file(spider.queue_file, spider.queue)
        set_to_file(spider.crawled_file, spider.crawled)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue: " + str(len(spider.queue)) + "| Crawled: " + str(len(spider.crawled)))
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.queue.remove(page_url)
            spider.crawled.add(page_url)
            spider.update_spider_file()

