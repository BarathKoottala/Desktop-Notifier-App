import requests
import xml.etree.ElementTree as ET 
from auth import get_auth

# url of google news rss feed alert

RSS_FEED_URL = "https://www.reddit.com/r/UpliftingNews.rss"

PERSONAL_RSS_FEED  = "https://www.reddit.com/.rss?feed=d0bfd27c336002ab487a1bf8df3dd69ec15e61ed&user=grahamaubrey"

secret = "MV2mvGD7qV8fFZv-Mrz2xkxL-ETEnw"

def load_rss_feed():
    """Function to load RSS feed from Uplifting News SubReddit"""

    params = get_auth()

    resp = requests.get(PERSONAL_RSS_FEED, auth="")

    return resp.content


def parse_xml(rss):
    """Function to parse XML rss feed"""
    breakpoint()
    root = ET.fromstring(rss)

    uplifting_news_items = []

    for child in root:
        print(child.tag, child.attrib)

    breakpoint()

    for item in root.findall('entry'):
        # breakpoint()
        news = {}

        for child in item:

            if child.tag == 'link':
                news["link"] = child.text.encode('utf8')
            if child.tag == 'title':
                news["title"] = child.text.encode('utf8')

            uplifting_news_items.append(news)
        
    
    return uplifting_news_items


def get_top_stories():

    rss = load_rss_feed()

    # reddit_content

    newsitems = parse_xml(rss)

    return newsitems
