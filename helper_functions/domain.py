from urllib.parse import urlparse

#Get last two tokens from the url domain name
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split(".")
        return results[-2]+"."+results[-1]
    except:
        return ""

#get the whole domain name
def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""

