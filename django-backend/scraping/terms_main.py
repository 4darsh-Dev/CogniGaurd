from bs4 import BeautifulSoup
import requests
import pandas as pd


# URL of the page we want to scrape
myUrls = [
    # add entries
    "https://onionreads.com/terms-and-conditions/",

]

for url in myUrls:
    # Get the HTML content of the page
    page = requests.get(url)
    html_doc = page.text
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_doc, 'html.parser')

    soup = soup.prettify()
    print(soup)


    
