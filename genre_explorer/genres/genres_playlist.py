from .models import Genre
from .genres_scraper import create_genres_dictionary
from .constants import API_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION   
from apiclient.discovery import build
from apiclient.errors import HttpError

def create_genres_from_dictionary():
    """
    Returns a sorted list of Genre objects from the dictionary of genres
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    dict_of_genre = create_genres_dictionary()
    list_of_genres = []
    dict_keys = sorted(dict_of_genre.keys())
    for i in dict_keys:
        tmp = dict_of_genre[i]
        for j in tmp:
            search_response = youtube.search().list(
                q=j,
                part="snippet",
                type="playlist",
                maxResults=1
            ).execute()
            
            
            for result in search_response.get("items", []):
                playlist_id = str(result["id"]["playlistId"])
                
                playlist_response = youtube.playlists().list(
                part="player",
                id=playlist_id,
                maxResults=1
                ).execute()
                for playlist_res in playlist_response.get("items", []):
                    genre = Genre(
                        name=j,
                        playlist_embed_tag=playlist_res["player"],
                        playlist_url="None"
                    )
                    list_of_genres.append(genre)
                
    list_of_genres.sort(key=lambda x: x.name, reverse=True)
    return list_of_genres
if __name__ == '__main__':
        create_genres_from_dictionary()