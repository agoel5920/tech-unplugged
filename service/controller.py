import sys
from content import ContentService
from whatsapp import WhatsAppService
from llm import LLMService
from dotenv import load_dotenv
import os

def main(index):
    
    load_dotenv()
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    
    queries = [
        f"https://newsapi.org/v2/everything?q='AI'&searchIn=title,description&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
        f"https://newsapi.org/v2/everything?q='LLM'&searchIn=title,description&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
        f"https://newsapi.org/v2/everything?q='SAAS'&searchIn=title,description&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
        f"https://newsapi.org/v2/everything?q='API'&searchIn=title,description&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
        f"https://newsapi.org/v2/everything?domains=techcrunch.com&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
        f"https://newsapi.org/v2/top-headlines?category=technology&language=en&from=2025-02-08&sortBy=popularity&apiKey={NEWS_API_KEY}",
    ]

    query = queries[index]

    whatsapp_service = WhatsAppService()

    llm_service = LLMService(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={GEMINI_API_KEY}")
    content_service = ContentService(query)
    
    data = content_service.fetch_data()
    articles = data.get('articles', [])[:5]  # Get the first 5 articles
    
    summary = llm_service.pick_and_summarize_best_article(articles)
    summary.replace('\n', '\r')
    whatsapp_service.send_message(summary)
    
    whatsapp_service.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python controller.py <index>")
    else:
        main(int(sys.argv[1]))
