from scraping_htmlwebsite.get_data import html_decoded_text
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

# Paramêtres du Chatbot
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzNmYWJhNGUtZDE1NS00N2M4LThjNzUtMGMyNDU5Mjk1ZmQwIiwidHlwZSI6ImFwaV90b2tlbiJ9.xgPtY8eTTtMfNUi-9MKE2cB8PDehR-B2kczHpfPxCs0"}

url = "https://api.edenai.run/v2/text/chat"


# Récupération des données textuelles du site
html_url = "http://localhost:8001/"

def get_soup(html_url):
    response = requests.get(html_url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to retrieve the page '{html_url}'. Status code: {response.status_code}")

page_soup = get_soup(html_url)

html_soup = page_soup.find_all("p")

# Fix character encoding issue
html_decoded_text = [p.text.encode('latin1').decode('utf-8') for p in html_soup]



provider = "meta"
prompt = ""
data = html_decoded_text

# Previous history
previous_history = []


payload = {
    "providers": provider,
    "text": f"{prompt}",
    "chatbot_global_action": f"Act like an assistant with this :{data} and {previous_history}",
    "previous_history": [],
    "temperature": 0.8,
    "max_tokens": 150,
    "fallback_providers": ""
}
# Paramêtres du Chatbot

