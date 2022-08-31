import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def news():
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=c16715a456f64335a3a7c582cbe2a202"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")




# def news():
#     main_url ="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c16715a456f64335a3a7c582cbe2a202"
#     main_page = requests.get(main_url).json()
#     # print(main_page)
#     articles = main_page["articles"]
#     # print(articles)
#     head=[]
#     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","nighth","tenth"]
#     for ar in articles:
#         head.append(ar["title"])
#     # print(head)
#     for i in range(len(day)):
#         print(f"today's {day[i]} news is : {head[i]} ")
#         speak(f"today's {day[i]} news is : {head[i]} ")