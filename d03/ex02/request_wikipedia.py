#!/usr/bin/python3

import requests, json, sys, dewiki

def request_wikipedia():
    if(len(sys.argv) != 2):
        print("Wrong number of arguments! Expected exactly one.")
        return
    url = "https://en.wikipedia.org/w/api.php"
    search_term = sys.argv[1]
    adjusted_search_term = search_term.strip().replace(' ', '_')
    try:
        data = requests.get(url, params={'action':'query', 'list':'search', 'format':'json', 'srsearch': search_term})
        print(data.text)
    except requests.HTTPError as e:
        return print(e)
    try:
        page_id = json.loads(data.text)["query"]["search"][0]["pageid"]
    except IndexError:
        try:
            search_term = json.loads(data.text)["query"]["searchinfo"]["suggestion"]
        except KeyError:
            return print("Search term not found.")
        try:
            data = requests.get(url, params={'action':'query', 'list':'search', 'format':'json', 'srsearch': search_term})
            page_id = json.loads(data.text)["query"]["search"][0]["pageid"]
        except requests.HTTPError as e:
            return print(e)   
    try:
        first_result = requests.get(url, params={'action':'parse', 'pageid': page_id, 'prop':'wikitext', 'format':'json'})    
    except requests.HTTPError as e:
        return print(e)       
    try:
        wiki_content = dewiki.from_string(json.loads(first_result.text)["parse"]["wikitext"]["*"])
        with open("{}.wiki".format(adjusted_search_term), "w") as f:
            f.write(wiki_content)
    except Exception as e:
        return print(e)

if __name__ == '__main__':
    request_wikipedia()