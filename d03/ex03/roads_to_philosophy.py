#!/usr/bin/python3

import sys, requests
from bs4 import BeautifulSoup

def roads_to_philosophy():
    if(len(sys.argv) != 2):
        return print("Wrong number of arguments !")
    previous_pages=[]
    page_title = sys.argv[1]
    search_term=sys.argv[1].strip().replace(" ", "_")
    search_url = "wiki/" + search_term
    while(page_title != "Philosophy"):
        url = "https://en.wikipedia.org/" + search_url
        try:
            data = requests.get(url)
            data.raise_for_status()
        except requests.HTTPError as e:
            if(data.status_code == 404):
                return print("It's a dead end !")
            return(print(e))
        soup=BeautifulSoup(data.text, "html.parser")
        page_title = soup.find(id="firstHeading").text
        if page_title in previous_pages:
            return print("It leads to an infinite loop !")
        previous_pages.append(page_title)
        print(page_title)
        page_content = soup.find(id="mw-content-text")
        page_links = page_content.select("p > a")
        prev_search_url = search_url
        for link in page_links:
            if link.get("href") is not None and \
                link["href"].startswith("/wiki/") and \
                not link["href"].startswith("/wiki/Wikipedia:") and \
                not link["href"].startswith("/wiki/Help:"):
                search_url = link["href"]
                break
        if search_url == prev_search_url:
            return(print("It leads to a dead end !."))
    print(str(len(previous_pages)) + " roads from " + previous_pages[0] + " to philosophy !")

if __name__ == '__main__':
    roads_to_philosophy()