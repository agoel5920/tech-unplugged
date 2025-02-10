import requests
import re

class LLMService:
    def __init__(self, llm_api_url):
        self.llm_api_url = llm_api_url

    def pick_and_summarize_best_article(self, articles):
        prompt = "Given the following articles, pick the best article:\n\n"
        for i, article in enumerate(articles):
            prompt += f"{i+1}. Title: {article['title']}\nDescription: {article['description']}\nURL: {article['url']}\n\n"
        prompt += "Return the summary of the best article. Use the URL to get the full article if needed. Format the summary so that it can be directly posted in a WhatsApp message. Keep it engaging. Avoid using characters outside the Basic Multilingual Plane (BMP). Include the URL of the article only once at the end."

        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'contents': [{
                'parts': [{'text': prompt}]
            }]
        }
        try:
            response = requests.post(self.llm_api_url, headers=headers, json=data)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            json_response = response.json()
            # print("Raw LLM response:", json_response)  # Print the raw response for inspection
            summary_text = json_response.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
            clean_summary_text = re.sub(r'[\U00010000-\U0010FFFF]', '', summary_text)  # Remove emojis above BMP
            print(summary_text)
            return clean_summary_text

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return "Request failed"

# Example usage:
# llm_service = LLMService("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=AIzaSyDxn6oN36LeFfyA2BNem3ZMbNwMgwT1jBY")
# llm_service = LLMService("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key=AIzaSyDxn6oN36LeFfyA2BNem3ZMbNwMgwT1jBY")
# articles = [
#         {
#             "title": "Galaxy S25 and S25 Plus Review: AI That's Enjoyable Without Being Overwhelming",
#             "description": "Samsung's new phones deliver on cameras and battery life, but AI is finally finding its footing, too.",
#             "url": "https://www.cnet.com/tech/mobile/galaxy-s25-and-s25-plus-review-ai-thats-enjoyable-without-being-overwhelming/",
#             "urlToImage": "https://www.cnet.com/a/img/resize/e49f3c7952d945e141e8b7d0af8b8d401aa7f9be/hub/2025/01/29/b04a5239-1672-4d5e-b1fc-30cfd1c27add/samsung-galaxy-s25-s25-plus-9408.jpg?auto=webp&fit=crop&height=675&width=1200",
#             "publishedAt": "2025-02-08T13:00:17Z",
#             "content": "Samsung's mantra when debuting the Galaxy S25 and S25 Plus appears to have been, \"If it ain't broke, don't fix it,\" as this year's phones share a striking resemblance to last year's S24 and S24 Plus.… [+20296 chars]"
#         },
#         {
#             "title": "VCs are eager to back a new wave of AI-powered robots. Here are 12 startups in the space to watch.",
#             "description": "The next wave of AI robotics startups transforming healthcare and logistics will include these 12 companies that have raised VC money last year.",
#             "url": "https://www.businessinsider.com/ai-robotics-startups-to-watch-as-vcs-invest-spatial-intelligence-2025-2",
#             "urlToImage": "https://i.insider.com/67a23ad67bb3f854015ba9f0?width=1200&format=jpeg",
#             "publishedAt": "2025-02-08T10:00:02Z",
#             "content": "Getty Images; Jenny Chang-Rodriguez/BI\r\n<ul><li>VCs are excited to invest in a new wave of robotics startups that use AI and spatial intelligence.</li><li>BI compiled a list of startups to watch in t… [+5923 chars]"
#         },
#         {
#             "title": "Microsoft Edge Gets a \"Scareware\" Blocker to Stop Fake Alert Sites",
#             "description": "This new AI-powered feature can stop \"scareware,\" the type of scam that pretends to be saving you from malware.",
#             "url": "https://www.makeuseof.com/microsoft-edge-scareware-blocker-for-fake-alerts/",
#             "urlToImage": "https://static1.makeuseofimages.com/wordpress/wp-content/uploads/2024/09/a-close-up-shot-of-microsoft-edge-running-on-a-laptop.jpg",
#             "publishedAt": "2025-02-08T02:07:52Z",
#             "content": "While all scams are scary, \"scareware\" can be the worst of its kind, masquerading as a service to save you from a malware attack. To mitigate these types of scams, Microsoft has added a \"scareware bl… [+2944 chars]"
#         },
#         {
#             "title": "Three fundamental principles for the future of AI policymaking: have a clear view of reality, be pragmatic instead of ideological, and empower the AI ecosystem (Fei-Fei Li/Financial Times)",
#             "description": "Fei-Fei Li / Financial Times:\nThree fundamental principles for the future of AI policymaking: have a clear view of reality, be pragmatic instead of ideological, and empower the AI ecosystem  —  It is possible to develop a model with the best intentions, and f…",
#             "url": "https://www.techmeme.com/250208/p4",
#             "urlToImage": "https://www.ft.com/__origami/service/image/v2/images/raw/https%3A%2F%2Fd1e00ek4ebabms.cloudfront.net%2Fproduction%2F22bbd3cd-733a-49eb-baf5-c09970189141.jpg?source=next-article&fit=scale-down&quality=highest&width=700&dpr=1",
#             "publishedAt": "2025-02-08T06:40:01Z",
#             "content": "About This Page\r\nThis is a Techmeme archive page.\r\nIt shows how the site appeared at 2:05 AM ET, February 8, 2025.\r\nThe most current version of the site as always is available at our home page.\r\nTo v… [+70 chars]"
#         },
#         {
#             "title": "‘A Complete Unknown’ Used AI? Your iPhone Photos Use More AI Than Any 2025 Oscar Nominee",
#             "description": "As Oscars consider AI mandatory disclosure requirement, there's more AI used in your iPhone photos than 2025's Best Picture nominees.",
#             "url": "https://www.indiewire.com/news/analysis/oscars-consider-ai-disclosure-a-complete-unknown-1235093013/",
#             "urlToImage": "https://www.indiewire.com/wp-content/uploads/2024/12/MCDCOUN_H4007.jpg?w=650",
#             "publishedAt": "2025-02-08T00:23:53Z",
#             "content": "The Academy might require future Oscar submissions to disclose their use of artificial intelligence tools, IndieWire has learned — but what does that mean when AI is, well, everywhere?\r\nVariety repor… [+4034 chars]"
#         }
#     ]
# summary = llm_service.pick_and_summarize_best_article(articles)
# # print("Summary:", summary)
