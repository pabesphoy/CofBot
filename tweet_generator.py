from playwright.async_api import async_playwright
from config import TWITTER_USERNAME, TWITTER_PASSWORD
import asyncio
import time
import random



async def scroll_down(page, delay=1):
    res = set()
    scrolls = 10
    
    for i in range(scrolls):
        scroll_size = str(random.randint(500, 5000))
        print('Scroll', i , 'de ', scrolls)
        await page.evaluate('window.scrollBy(0, ' + scroll_size + ');')  # Desplazarse hacia abajo una pantalla
        await asyncio.sleep(delay)  # Espera para que se carguen más tweets
        tweets = await page.query_selector_all('article[data-testid="tweet"]')
        for t in tweets:
            tweet_text = await t.inner_text()
            print('Tweet detectado: ', tweet_text)
            if '@fuwasnow2' not in tweet_text:
                continue
            tweet_text_element = await t.query_selector('div[lang]')
            if tweet_text_element:
                tweet_text = await tweet_text_element.inner_text()
                res.add(tweet_text)
    print('Tweets totales: ', res)
    return res

async def get_tweets():
    res = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://twitter.com/login")

        await page.wait_for_selector("input[name='text']", timeout=10000)

        await page.fill("input[name='text']", TWITTER_USERNAME) 
        await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']") 
        
        await page.wait_for_selector("input[name='password']", timeout=10000)
        
        await page.fill("input[name='password']", TWITTER_PASSWORD)  
        await page.click("button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']") 
        await page.goto("https://twitter.com/fuwasnow2")

        time.sleep(10)

        print('Scrollenando...')
        res = await scroll_down(page)
        return list(res)

async def generate_tweet(phrases):
    tweet = ""
    tweets = set()
    numero_tweets = random.randint(1,5)
    while(tweets.__len__() < numero_tweets):
        tweets.add(phrases[random.randint(0, phrases.__len__() - 1)])
    print('tweets elegidos: ' , tweets)

    for t in tweets:
        t_array = t.split(" ")
        num_palabras = random.randint(2, 8)
        palabra_inicial = random.randint(0, len(t_array) - 1)
        
        if t_array.__len__() >  num_palabras + palabra_inicial:
            for i in range(palabra_inicial, palabra_inicial + num_palabras):
                tweet += t_array[i] + " "
        else:
            for i in range(palabra_inicial, len(t_array)):
                tweet += t_array[i] + " "
    
    return tweet