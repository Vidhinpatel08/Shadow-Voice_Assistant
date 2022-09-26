import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def news():
    speak("News for today.. Lets begin")

    # today_url = f'https://newsapi.org/v2/everything?q=apple&from={year}-{month}-{day}&to={year}-{month}-{day}&sortBy=popularity&apiKey=c16715a456f64335a3a7c582cbe2a202'
    # the-times-of-india = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=c16715a456f64335a3a7c582cbe2a202"
    in_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c16715a456f64335a3a7c582cbe2a202"

    news = requests.get(in_url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak(f'We have Total {len(arts)} news.')
    for i,article in enumerate(arts):
        arg = f"News {i+1} is {article['title']}"
        print(arg)
        speak(arg)

if __name__ == "__main__":
    news()

