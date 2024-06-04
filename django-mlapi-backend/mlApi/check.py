import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import cmudict
from tqdm import tqdm

import csv

# for downloding the necessary data for nltk
# nltk.download('punkt')
# nltk.download('cmudict')


# Load the CMU Pronouncing Dictionary
try:
    cmu_dict = cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    cmu_dict = cmudict.dict()

def count_syllables(word):
    global cmu_dict
    
    if word.lower() in cmu_dict:
        return max(len(list(y for y in x if y[-1].isdigit())) for x in cmu_dict[word.lower()])
    else:
        # Fallback: Estimate syllables based on the number of vowels
        vowels = "aeiouy"
        return sum(1 for char in word.lower() if char in vowels)
    
    
def flesch_reading_ease(text):
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # Count syllables using the CMU Pronouncing Dictionary
    syllables = sum(count_syllables(word) for word in words)

    # Count words and sentences
    num_words = len(words)
    num_sentences = len(sentences)

    # Calculate the Flesch Reading Ease score
    flesch_score = 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (syllables / num_words)

    return flesch_score

# Example usage:

# reading from this file
terms_file = "F:/backup-kali/codeFiles/projects/CogniGuard-API/datasets/terms.csv"

# writing to this file
terms_dataset = "F:/backup-kali/codeFiles/projects/CogniGuard-API/datasets/terms_datset.csv"

with open(terms_file , "r") as f:
    rows = csv.DictReader(f)
    for row in rows:
        terms_and_conditions_text = row['terms_and_conditions']
        
        score = flesch_reading_ease(terms_and_conditions_text)
    
        print(f"Flesch Reading Ease Score: {score}")






