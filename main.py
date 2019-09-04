from mastodon import Mastodon
import os, time

# Initialize
api = Mastodon(os.getenv('CLIENT_KEY'), os.getenv('CLIENT_SECRET'), os.getenv('ACCESS_TOKEN'), os.getenv('POD'))
min_id = ''

while True:
    # Get local timeline of the pod
    # timeline = api.timeline(timeline='local')
    timeline = api.timeline_local(min_id=min_id)

    # Iterate through toots in timeline and fav them
    for toot in timeline:
        api.status_favourite(toot['id'])

    min_id = timeline[0]['id']

    time.sleep(30)
