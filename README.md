# Scraper

![](http://i.imgur.com/wYi2CkD.png)

# Overview

Multi-threaded web crawler written in Python.

```
Scrapper/
├── crawler/
│   └── main.py
│  
├── helper_functions/
│   ├── domain.py
│   ├── files_manager.py
│   └── link_finder.py
│
├── Spider/
│   └── spider.py
│
└── projects/
    ├── 
    └── 
```

The ```link_finder.py``` is the file in which we gather the links out of an HTML code.

The ```spider.py``` is the file in which all the spiders can manage to get pages to crawl

The ```start_multithreading_crawling.py``` This is where we create all the workers, each worker has the job, and we start crawling by getting all the urls mentioned in the links' HTML code from the queue.
