import requests
from bs4 import BeautifulSoup


# Parsing info from pages
def parsing_info():
    """ Parsing info from pages """

    """
    parsing urls
    pages
    """
    url = 'https://workspace.ru/events/meetup/'
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "lxml")
    url_conf = soup.find_all("a", class_="events-list-item__title")
    urls = list()
    for url in url_conf:
        urls.append('https://workspace.ru'+url.get('href'))
        

    """
    parsing info
    from pages
    """
    info = list()
    for link in urls:
        r = requests.get(url=link)
        soup = BeautifulSoup(r.text, "lxml")
        name = soup.find("h1", class_="event-detail__title")
        conf_info = soup.find("div", class_="event-detail__content")
        info.append([name.text, conf_info.text])
    
    """ 
    Return list of 
    the names and
    discriptions of 
    the conferences 
    """
    return info