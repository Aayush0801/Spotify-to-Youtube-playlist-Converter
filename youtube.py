from ytmusicapi import YTMusic, OAuthCredentials
import os
import requests as r
client_id = os.getenv('youtube_client_id')
client_secret = os.getenv('youtube_client_secret')

def get_first_valid_video_id(search_results):
    for res in search_results:
        if 'videoId' in res:
            return res['videoId']
    return None


url = "http://localhost:8080/api/music"

ytmusic = YTMusic("oauth.json",oauth_credentials= OAuthCredentials(client_id= client_id, client_secret= client_secret))


response = r.get(url=url)
data = response.json()

playlist_set = dict()


for song in data:
    playlist_name = song["playlist_name"].strip()
    song_name = song["song_name"].strip()

    if not song_name:
        print(f"Skipping empty or invalid song name in playlist '{playlist_name}'")
        continue

    search_results = ytmusic.search(song_name)
    videoId = get_first_valid_video_id(search_results)
    if playlist_name in playlist_set:
        
        if videoId:
            ytmusic.add_playlist_items(playlist_set[playlist_name], [videoId])
            print(f"Added {song_name} to {playlist_name}")
        else:
            print(f"Couldn't find a video for {song_name}")
    else:
        playlistId = ytmusic.create_playlist(playlist_name, "No description")
        playlist_set[playlist_name] = playlistId
        if videoId:
            ytmusic.add_playlist_items(playlistId, [videoId])
            print(f"Added {song_name} to {playlist_name}")
        else:
            print(f"Couldn't find a video for {song_name}")
         



