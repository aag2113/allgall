import spotipy

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
	def handle(self, *args, **options):
		PLAYLIST_ID_100 = settings.PLAYLIST_ID_100
		SPOTIFY_O_AUTH_TOKEN = settings.SPOTIFY_O_AUTH_TOKEN

		try:
			sp = spotipy.Spotify(auth=SPOTIFY_O_AUTH_TOKEN)
		except:
			print('OAuth token expired')
		tracks_1 = sp.current_user_saved_tracks(limit=50)
		tracks_2 = sp.current_user_saved_tracks(limit=50, offset=50)

		track_ids = [track.get('track').get('id') for track in tracks_1.get('items')]
		track_ids.extend([track.get('track').get('id') for track in tracks_2.get('items')])
		sp.user_playlist_replace_tracks("adam.gall", PLAYLIST_ID_100, track_ids)
