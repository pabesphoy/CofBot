import random
from tweet_generator import generate_tweet, get_tweets

async def post_to_bluesky(client):
    try:
        tweets = await get_tweets()
        t = await generate_tweet(list(tweets))
        print(t)
        client.send_post(t)
        print(f"Publicado: {t}")
    except Exception as e:
        print(f"Error al publicar: {e}")
