import bs4, requests, re, string, collections

list_of_letters = list(string.ascii_uppercase)
list_of_letters.append("#")
genres = {k: [] for k in list_of_letters}

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
    
for genre in g:
    if genre[0] in genres:
        genres[genre[0]].append(genre)
    else:
        genres["#"].append(genre)
   
print(genres)