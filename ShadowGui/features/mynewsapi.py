import requests
import json
import time
import features.TTS as TTS
import difflib

API_KEY = "abea9e451b5c436195dad057bcafef0b" # {if you want to pass by secure folder then it good}


def is_related(word, categories):
    close_matches = difflib.get_close_matches(word, categories, n=1, cutoff=0.6)
    return len(close_matches) > 0

def get_news_by_date(startDate,endDate):
        url = f"https://newsapi.org/v2/top-headlines?q=all&from={startDate}&to={endDate}&sortBy=popularity&country=in&apiKey={API_KEY}"
        response = requests.get(url).text
        news_data = json.loads(response)
        articles = news_data["articles"]
        TTS.speak_Print(f'We have Total {len(articles)} news.')
        
        for i,article in enumerate(articles):
            arg = f"News {i+1} is {article['title']}".replace(' - ',' Published BY ')
            TTS.speak_Print(arg)
        TTS.speak('News Completed, Now I am ready for next command')

def get_news_by_category(category):
        category = category.replace('"','').replace("'","")
        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
        response = requests.get(url).text
        news_data = json.loads(response)
        articles = news_data["articles"]
        TTS.speak_Print(f'We have Total {len(articles)} news.')
        
        for i,article in enumerate(articles):
            arg = f"News {i+1} is {article['title']}".replace(' - ',' Published BY ')
            TTS.speak_Print(arg)
        TTS.speak('News Completed, Now I am ready for next command')

            
def play_news(query):
    categories= ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    category = None
    for word in query.split(' '):
        if is_related(word, categories):
            category = word
            break
        # elif word in ['today','todays','day','month','any']:
        #     if word.startswith('tod'):
        #         seconds = time.time()
        #         result = time.gmtime(seconds)
        #         year,month,day = result.tm_year,result.tm_mon,result.tm_mday
        #         startDate,endDate =f'{year}-{month}-{day}', f'{year}-{month}-{day}'
        #     else:
        #         startDate,endDate ='2023-02-10', '2023-02-10' # logic
        #     get_news_by_date(startDate,endDate)
        #     return


    if category != None and category != ' ':
        get_news_by_category(category)
        return

    # If the user's query does not specify a valid category,
    TTS.speak_Print(f"\nPlease specify a category {categories}")
    category = TTS.takeCommand_template()
    print("category: ",category)
    for Newscategories in categories:
        if category in Newscategories:
            get_news_by_category(category)
        elif is_related(category, Newscategories):
            get_news_by_category(category)
        else:
            TTS.speak_Print("\nInvalid category, See General News\n")
            get_news_by_category(category= 'general')
            return
    
        

if __name__ == "__main__":
    play_news("play news of today")
    print('Done')
