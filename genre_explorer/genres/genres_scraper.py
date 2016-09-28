import bs4, requests, string, re
from .constants import LIST_OF_LETTERS

def _get_links_to_sections_of_genres():
    """
    Returns a list of links to the different sections of genres in wikipedia
    """
    page_text = requests.get("https://en.wikipedia.org/wiki/List_of_music_styles")
    try:
        page_text.raise_for_status
    except Exception as exc:
        print("There was a problem")
        
    page_text = page_text.text
    bs_obj = bs4.BeautifulSoup(page_text, "html.parser")
    links_to_genres = bs_obj.findAll(href=re.compile("List_of_styles_of_music:_[A-Z].[A-Z]"))
    links = []
    for i in links_to_genres:
        links.append("https://en.wikipedia.org" + i.get("href"))
        
    return links
   

def _get_list_of_genre_from_links():
    """
    Returns the list of genres from the given list of links
    :params links - list
    """
    links = _get_links_to_sections_of_genres()
    g = []
    for i in links:
        wiki_genres_page = requests.get(i)
        try:
            wiki_genres_page.raise_for_status
        except Exception as exc:
            print("There was a problem")
        wiki_genres_page = wiki_genres_page.text
        bs_obj = bs4.BeautifulSoup(wiki_genres_page, "html.parser")
        for div in bs_obj.findAll("div", {"class": "navbox"}):
            div.decompose()
        bs_obj.p.decompose()
        
        tmp1 = bs_obj.select(".mw-content-ltr ul li")
        for i in tmp1:
            g.append(str(i.next_element.next_element))
        
        del g[len(g)-1]
        
    return g
    
def create_genres_dictionary():
    """
    Returns a dictionary of genres where the keys are the alphabet and the values
    a list of genres
    :params list_of_genres - list
    """
    list_of_genres = _get_list_of_genre_from_links()
    
    genres = {k: [] for k in LIST_OF_LETTERS}
    
    for genre in list_of_genres:
        if 'Sections' in genre or 'Section' in genre:
            list_of_genres.remove(genre)
        if genre[0] in genres:
            genres[genre[0]].append(genre)
            genres[genre[0]].sort()
        else:
            genres["#"].append(genre)
            genres["#"].sort()
            
    return genres