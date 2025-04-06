import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyPKCE
import os
import json
import requests as r


# auth_manager = SpotifyPKCE(client_id= os.getenv('client_id'),
#                            redirect_uri= "http://localhost",
#                            scope='playlist-read-private playlist-read-collaborative')

# gives you the acess to the spotify module using the client_id and the client_secret 
sp = spotipy.Spotify(client_credentials_manager= SpotifyOAuth(client_id= os.getenv("client_id"),
                                                              client_secret= os.getenv("client_secret"),
                                                              redirect_uri= 'http://localhost'))

pl1  = sp.current_user_playlists(limit= 50)
                            
headers = {'Content-type' : 'application/json'}
url = "http://localhost:8080/api/music"

# got the playlist info 
pl1 = sp.current_user_playlists(limit = 50)

for a in pl1['items']:
    
    pl_id = a['id']
    pl2 = sp.playlist(playlist_id = pl_id)
    pl_name = a['name']
    for b in pl2['tracks']['items']:
        if b['track']:
            data = {
                'song_name': b['track']['name'],
                'playlist_name': pl_name
            }
            data_payload = json.dumps(data)
            req = r.post(url,data = data_payload,headers= headers)
            print(req.status_code)
            



