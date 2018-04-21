from queue import Queue

from Spider.spider import spider
from helper_functions.domain import *
from helper_functions.link_finder import *
from helper_functions.files_manager import *

PROJECT_NAME = 'projects/wildml'
HOME_PAGE = 'http://www.wildml.com/'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()

spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

#Get someone to crawl for you
def create_workers():
    pass

#Get something to crawl it
def create_jobs():
    queue.join()
    crawl()


#Checks if there are any links in the queue, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue.")
        queue.put(queued_links)
        create_jobs()



