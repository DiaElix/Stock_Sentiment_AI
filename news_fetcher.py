import pandas as pd
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import os

from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")
# Load key from environment (simulated here for simplicity)

newsapi = NewsApiClient(api_key=API_KEY)

def get_market_news(query='NVIDIA'):
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    print(f"Fetching news for {query}...")
    
    articles = newsapi.get_everything(q=query, from_param=yesterday, language='en', sort_by='relevancy')
    
    data = [{'published_at': a['publishedAt'], 'title': a['title']} for a in articles['articles']]
    df = pd.DataFrame(data)
    df.to_csv('news_data.csv', index=False)
    print(f"Saved {len(df)} headlines to news_data.csv")

if __name__ == "__main__":
    get_market_news('NVIDIA')