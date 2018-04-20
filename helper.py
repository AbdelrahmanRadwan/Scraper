import os

'''
Files manipilation stuff...
'''
#Write contnt to a new file
def write_file(path, content):
    with open(path, "w") as file:
        file.write(content+"\n")
#Append something to existing file
def append_to_file(path, content):
    with open(path, "a") as file:
        file.write(content+"\n")
#Delete all the content in a file
def delete_file_content(path):
    with open(path, "w") as file:
        pass
#Return all the unique URLs in a file.
def file_to_set(path):
    unique_links = set()
    with open(path, "rt") as file:
        for link in file:
            unique_links.add(link.strip('\n'))
    return unique_links
#Write the unique links that we have to a file
def set_to_file(path, links):
    delete_file_content(path)
    sorted(links)
    for link in links:
        write_file(path, link)

#Create new project to crawl stuff in
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating new project at %s" %directory)
        os.makedirs(directory)
#Create crawling and queue files...
def create_data_files(project_name, home_page):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        append_to_file(queue, home_page)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

create_data_files("x", "google.com")