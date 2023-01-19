from time import sleep

import requests
from parsel import Selector

from tech_news.database import create_news


def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"},
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css(".post-inner header h2 a::attr(href)").getall()
    return news_links


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_next_page = selector.css(".nav-links a.next::attr(href)").get()
    return link_next_page


# https://stackoverflow.com/questions/3398852/using-python-remove-html-tags-formatting-from-a-string
def striphtml(data):
    import re

    p = re.compile(r'<.*?>')
    return p.sub('', data)


def scrape_news(html_content):
    selector = Selector(text=html_content)
    dict_news = dict()
    dict_news["url"] = selector.css(
        'head link[rel=canonical]::attr(href)',
    ).get()
    dict_news["title"] = selector.css("h1.entry-title::text").get().strip()
    dict_news["writer"] = selector.css("span.author a::text").get()
    dict_news["summary"] = striphtml(
        selector.css(".entry-content p").get()
    ).strip()
    dict_news["tags"] = selector.css("a[rel=tag]::text").getall()
    dict_news["category"] = selector.css(
        "a.category-style span.label::text",
    ).get()

    news_time = selector.css("ul.post-meta .post-modified-info::text").get()
    if news_time is None:
        news_time = selector.css("li.meta-date::text").get()
        dict_news["timestamp"] = news_time
    else:
        dict_news["timestamp"] = news_time.split(" ")[0]

    comments = selector.css("div.post-comments h5::text").get()
    if comments is None:
        dict_news["comments_count"] = 0
    else:
        dict_news["comments_count"] = int(comments.split(" ")[0])
    return dict_news


def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    news = []
    news_links = []
    while len(news_links) < amount:
        html_content = fetch(url)
        news_links.extend(scrape_updates(html_content))
        url = scrape_next_page_link(html_content)
        if url is None:
            break

    for link in news_links[:amount]:
        html_content = fetch(link)
        news.append(scrape_news(html_content))

    create_news(news)
    return news
