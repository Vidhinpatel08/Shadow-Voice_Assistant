import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def news():
    speak("News for today.. Lets begin")
    # url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=c16715a456f64335a3a7c582cbe2a202"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c16715a456f64335a3a7c582cbe2a202"

    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")


# from newsapi import NewsApiClient
# def news():
#     newsapi = NewsApiClient(api_key='c16715a456f64335a3a7c582cbe2a202')

#     data = newsapi.get_top_headlines(q='fast and furious 9',
#                                      language='en',
#                                      page_size=5)

#     newsdata = data['articles']
#     for x, y in enumerate(newsdata):
#         print(f'{x}{y["description"]}')
#         speak((f'{x}{y["description"]}'))

#     speak("that's it for now i'll update you in sometime")
news()

