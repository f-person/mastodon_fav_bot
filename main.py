from mastodon import Mastodon
import os, time

# Initialize
api = Mastodon(os.getenv('CLIENT_KEY'), os.getenv('CLIENT_SECRET'), os.getenv('ACCESS_TOKEN'), os.getenv('POD'))
tootId = ''

while True:
    # Get local timeline of the pod
    # timeline = api.timeline(timeline='local')
    timeline = api.timeline_local(min_id=tootId)

    # Iterate through toots in timeline and fav them
    for toot in timeline:
        print(toot)
        
        # tootId is set here to then set min_id
        tootId = toot['id']
        api.status_favourite(tootId)

    time.sleep(30)
