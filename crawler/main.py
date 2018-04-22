from queue import Queue
import threading
from Spider.spider import spider
from helper_functions.domain import *
from helper_functions.link_finder import *
from helper_functions.files_manager import *


PROJECT_NAME = 'projects/quora'
HOME_PAGE = 'https://www.quora.com/profile/Abdelrahman-Hamdy-1'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()

spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

#Get someone to crawl for you
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        worker_thread = threading.Thread(target=work)
        worker_thread.daemon = True
        worker_thread.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#Get something to crawl it
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#Checks if there are any links in the queue, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " links in the queue.")
        create_jobs()



create_workers()
crawl()