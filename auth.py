from atproto import Client
from config import BSKY_USERNAME, BSKY_PASSWORD

def authenticate():
    client = Client()
    client.login(BSKY_USERNAME, BSKY_PASSWORD)
    return client
