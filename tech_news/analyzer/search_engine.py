from datetime import date as d

from tech_news.database import search_news


def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    news_formated_list = []
    for news in news_list:
        news_formated_list.append((news["title"], news["url"]))
    return news_formated_list


def search_by_date(date):
    try:
        formatted_date = d.strftime(d.fromisoformat(date), '%d/%m/%Y')
        news_list = search_news({"timestamp": {"$regex": formatted_date}})
        news_formated_list = []
        for news in news_list:
            news_formated_list.append((news["title"], news["url"]))
        return news_formated_list
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_formated_list = []
    for news in news_list:
        news_formated_list.append((news["title"], news["url"]))
    return news_formated_list


def search_by_category(category):
    news_list = search_news(
            {"category": {"$regex": category, "$options": "i"}}
        )
    news_formated_list = []
    for news in news_list:
        news_formated_list.append((news["title"], news["url"]))
    return news_formated_list
