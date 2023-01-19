from collections import Counter

from tech_news.database import search_news


def sort_by_comment(e):
    return e["comments_count"]


def top_5_news():
    news_list = search_news({})
    news_list.sort(key=sort_by_comment, reverse=True)
    if len(news_list) > 5:
        news_list = news_list[:5]
    list_formated = []
    for news in news_list:
        list_formated.append((news["title"], news["url"]))
    return list_formated


def top_5_categories():
    categories = []
    news_list = search_news({})
    for new in news_list:
        categories.append(new["category"])
    top_categories = [
        category[0] for category in Counter(sorted(categories)).most_common(5)
    ]
    return top_categories
