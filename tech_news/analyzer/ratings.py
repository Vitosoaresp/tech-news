from tech_news.database import search_news


def order_by_comment(e):
    return e["comments_count"]


# Requisito 10
def top_5_news():
    news_list = search_news({})
    news_list.sort(key=order_by_comment, reverse=True)
    if len(news_list) > 5:
        news_list = news_list[:5]
    list_formated = []
    for news in news_list:
        list_formated.append((news["title"], news["url"]))
    return list_formated


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
