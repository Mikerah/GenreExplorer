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
    for i in sorted(dict_of_genre.keys()):
        tmp = dict_of_genre[i]
        for j in tmp:
            search_response = youtube.search().list(
                q=j,
                part="id",
                type="playlist",
                maxResults=1
            ).execute()
            
            
            for result in search_response.get("items", []):
                playlist_id = str(result["id"]["playlistId"])
                
                playlist_response = youtube.playlistItems().list(
                    part="Snippet",
                    playlistId=playlist_id,
                    maxResults=1
                ).execute()
                
                for video_res in playlist_response.get('items', []):
                    genre = Genre(
                        name = j,
                        playlist_url = "http://www.youtube.com/watch?v=" \
                                        + str(video_res["snippet"]["resourceId"]["videoId"]) + "&list=" \
                                        + playlist_id
                    )
                    list_of_genres.append(genre)
    
    sorted(list_of_genres)
    return list_of_genres
if __name__ == '__main__':
        create_genres_from_dictionary()