import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from fake_useragent import UserAgent


import csv
import nltk
nltk.download('punkt')

## version 1

def get_scrape_data(url):
    
    # Use a fake user agent to mimic a web browser by adding header
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}

    # Making the request using the headers
    response = requests.get(url, headers=headers)

    
    if response.status_code == 200:
        html_text = response.text

        # Extracting the text
        soup = BeautifulSoup(html_text, 'html.parser')

        tags_list = ['div', 'span', 'p', 'a', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        # text = ' '.join([tag.get_text() for tag in soup.find_all(tags_list)])
        text_list = []

        # Use tqdm to display a progress bar
        for tag in tqdm(soup.find_all(tags_list), desc='Extracting Text', unit='tags'):
            text_list.append(tag.get_text())

        text = ' '.join(text_list)

        return text

    else:
        # Handle the case where the request was not successful
        print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
        return None


def paragraph_to_sentences(paragraph):
    # Tokenize the paragraph into sentences
    sentences = nltk.sent_tokenize(paragraph)
    return sentences



def save_sentences_to_csv(sentences, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['no', 'sentence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write each sentence along with its number
        for i, sentence in enumerate(sentences, 1):
            # Remove extra whitespace from the sentence
            cleaned_sentence = ' '.join(sentence.split())
            writer.writerow({'no': i, 'sentence': cleaned_sentence})

def dark_sentence_list(url):
    scraped_text = get_scrape_data(url)
    sentences = paragraph_to_sentences(scraped_text)
    save_sentences_to_csv(sentences, 'sentences.csv')
    successMsg = "Scraped data saved to sentences.csv"
    return successMsg, 'sentences.csv'



# sample url 
my_url = "https://www.amazon.in/BassHeads-122-Earphones-Tangle-Straight/dp/B07QZ3CZ48/ref=sr_1_1?crid=I50H5USKYCLC&keywords=wired%2Bearphones%2Bboat&qid=1705597770&sprefix=wired%2Bearphones%2B%2Caps%2C2763&sr=8-1&th=1"


