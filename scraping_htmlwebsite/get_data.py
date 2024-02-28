from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup

# Base URL
url = 'http://localhost:8001/'

# Mapping function to convert star ratings to numbers

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to retrieve the page '{url}'. Status code: {response.status_code}")

page_soup = get_soup(url)

html_soup = page_soup.find_all("p")


# Fix character encoding issue
html_decoded_text = [p.text.encode('latin1').decode('utf-8') for p in html_soup]

