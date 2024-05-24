# Saving the data to models.py from csv file as input

import pandas as pd
from home.models import FAQData

def save_from_csv(file_path):
    # Read the CSV file into a DataFrame
    faq_df = pd.read_csv(file_path)

    # Iterate over each row and save to FAQData model
    for index, row in faq_df.iterrows():
        FAQData.objects.create(question=row['question'], answer=row['answer'])

if __name__ == "__main__":
    file_path = "faqs.csv"
    save_from_csv(file_path)
