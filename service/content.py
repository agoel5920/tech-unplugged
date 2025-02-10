import requests

class ContentService:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# # Example usage:
# query = "https://newsapi.org/v2/everything?q='AI'&searchIn=title,description&language=en&from=2025-02-08&sortBy=popularity&apiKey=26b6d57c84dc45eca4bda16be04e0b08"
# content_service = ContentService(query)
# data = content_service.fetch_data()
# print(data)

