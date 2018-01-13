import spotipy
import spotipy.util as sputil

from django.core.management.base import BaseCommand
from django.conf import settings

from AllGall.utilities import send_mail


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = settings.SPOTIFY.get('user')
        scope = settings.SPOTIFY.get('scope')
        client_id = settings.SPOTIFY.get('client_id')
        client_secret = settings.SPOTIFY.get('client_secret')
        redirect_uri = settings.SPOTIFY.get('redirect_uri')
        playlist_id = settings.SPOTIFY.get('playlist_id')

        token = sputil.prompt_for_user_token(
            user,
            scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri
        )

        try:
            sp = spotipy.Spotify(auth=token)
        except:
            send_mail("Spotify Error", "Authentication Failure", "gall.adam@gmail.com")
            return

        tracks_1 = sp.current_user_saved_tracks(limit=50)
        tracks_2 = sp.current_user_saved_tracks(limit=50, offset=50)

        track_ids = [track.get('track').get('id') for track in tracks_1.get('items')]
        track_ids.extend([track.get('track').get('id') for track in tracks_2.get('items')])
        sp.user_playlist_replace_tracks(user, playlist_id, track_ids)
