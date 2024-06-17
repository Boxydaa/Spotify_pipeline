import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    client_credentials_manager = SpotifyClientCredentials(client_id = "579bb8e390414b4cbaab482e1feb1f69", client_secret = "86c809608e714e268315394d36a3e353")
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
    playlist_uri = playlist_link.split("/")[-1].split("?")[0]
    
    spotify_data = sp.playlist_tracks(playlist_uri)
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" +str(datetime.now())+ ".json"
    
    client.put_object(
        Bucket = "spotify-etl-rajesh-r",
        Key = "raw_data/to_processed/" + filename,
        Body = json.dumps(spotify_data)
        )
        

    
