import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyControl:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="ad6fdf08193b4775996ec9599deacde1",
            client_secret="d0f19ff999fb4322979c2f22089fa801",
            redirect_uri="http://localhost:8888/callback",
            scope="user-modify-playback-state user-read-playback-state"
        ))

    def play_song(self, track_name):
        results = self.sp.search(q=track_name, type='track', limit=1)
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            self.sp.start_playback(uris=[track_uri])
            print(f"Playing {track_name}")
        else:
            print(f"Could not find {track_name}")

    def pause(self):
        self.sp.pause_playback()

    def resume(self):
        self.sp.start_playback()

    def next_track(self):
        self.sp.next_track()

    def previous_track(self):
        self.sp.previous_track()

