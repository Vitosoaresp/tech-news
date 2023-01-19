from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news

options_dict = {
    '0': ('Digite quantas notícias serão buscadas: ', get_tech_news),
    '1': ('Digite o título: ', search_by_title),
    '2': ('Digite a data no formato aaaa-mm-dd: ', search_by_date),
    '3': ('Digite a tag: ', search_by_tag),
    '4': ('Digite a categoria: ', search_by_category),
    '5': top_5_news,
    '6': top_5_categories,
}


def analyzer_menu():
    option = input('''Selecione uma das opções a seguir:
        0 - Popular o banco com notícias;
        1 - Buscar notícias por título;
        2 - Buscar notícias por data;
        3 - Buscar notícias por tag;
        4 - Buscar notícias por categoria;
        5 - Listar top 5 notícias;
        6 - Listar top 5 categorias;
        7 - Sair.
    ''')

    if option == '7':
        print("Encerrando script")
        return
    elif option == '0':
        quantity = input(options_dict[option][0])
        options_dict[option][1](int(quantity))
        print("Banco populado com sucesso!")
        return
    elif option in ['5', '6']:
        selected = options_dict[option]
        return selected()
    elif option in ['1', '2', '3', '4']:
        search = input(options_dict[option][0])
        return(options_dict[option][1](search))
    else:
        print(ValueError('Opção inválida'))
        return

__name__ == '__main__' and analyzer_menu()
