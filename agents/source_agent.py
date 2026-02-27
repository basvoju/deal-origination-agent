import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL
from tools.news_tool import fetch_company_news

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

def source_agent():

    companies = fetch_company_news()

    return companies