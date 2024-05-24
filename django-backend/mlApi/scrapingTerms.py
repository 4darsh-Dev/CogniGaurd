import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import logging

# Configure logging
logging.basicConfig(filename='scraping_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_terms_and_conditions(url):
    logging.info(f'Scraping {url}')
    print(f'Scraping {url}')
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the heading tag that contains "Terms and Conditions"
        terms_heading = soup.find(lambda tag: tag.name and "terms and conditions" in tag.get_text().lower())

        if terms_heading:
            # Extract the content following the heading tag
            terms_and_conditions_text = ''
            current_tag = terms_heading.find_next()
            while current_tag and current_tag.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                terms_and_conditions_text += str(current_tag)
                current_tag = current_tag.find_next()

            return terms_and_conditions_text

        else:
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"Error while scraping {url}: {e}")
        return None
    
    

def save_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['website', 'terms_and_conditions']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in tqdm(data, desc='Scraping progress'):
            writer.writerow(row)


if __name__ == "__main__":
    websites = [
        # {'name': 'flipkart.com', 'url': 'https://www.flipkart.com/pages/terms'},
        # {'name': 'myntra.com', 'url': 'https://www.myntra.com/termsofuse'},
        # # {'name': 'amazon.in', 'url': 'https://www.amazon.in/gp/help/customer/display.html'},
        # {'name': 'wynk.in', 'url': 'https://wynk.in/music/tnc'},
        # {'name': 'linkedin.com', 'url': 'https://www.linkedin.com/legal/user-agreement'},
        # {'name': 'facebook.com', 'url': 'https://www.facebook.com/legal/terms/update'},
        # {'name': 'instagram.com', 'url': 'https://help.instagram.com/581066165581870'},
        # {'name': 'spotify.com', 'url': 'https://www.spotify.com/in-en/legal/end-user-agreement/'},
        {'name' : 'onionreads.com', 'url' : 'https://onionreads.com/terms-and-conditions/'}
    ]

    scraped_data = []

    print('Scraping process started...')

    for website in websites:
        terms_and_conditions_text = scrape_terms_and_conditions(website['url'])
        scraped_data.append({'website': website['name'], 'terms_and_conditions': terms_and_conditions_text})

    save_to_csv(scraped_data, 'terms_and_conditions_dataset.csv')

    print('Scraping process finished...')
