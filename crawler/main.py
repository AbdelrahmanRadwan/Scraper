import threading
from helper import *
from queue import Queue
from link_finder import LinkFinder
from domain import *
from spider import spider

PROJECT_NAME = "wildml"
HOME_PAGE = "www.wildml.com/"
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()

spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)
