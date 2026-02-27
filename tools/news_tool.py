import requests
from config import NEWS_API_KEY

def fetch_company_news():

    url = f"https://newsapi.org/v2/everything?q=startup OR acquisition OR AI&apiKey={NEWS_API_KEY}"

    response = requests.get(url)

    articles = response.json()["articles"]

    companies = []

    for article in articles[:10]:

        companies.append({
            "name": article["source"]["name"],
            "description": article["title"],
            "source": article["url"]
        })

    return companies