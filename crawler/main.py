from queue import Queue

from Spider.spider import spider
from helper_functions.domain import *

PROJECT_NAME = "projects/wildml"
HOME_PAGE = "www.wildml.com/"
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()

spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
