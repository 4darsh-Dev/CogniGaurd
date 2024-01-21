# import nltk

# nltk.download('cmudict')
import pandas as pd
file_path = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/dp_dataset.tsv"

df = pd.read_csv(file_path, sep='\t')

uniqueVal1 = df['Pattern Category'].unique()
uniqueVal2 = df['text'].unique()
uniqueVal3 = df['label'].unique()


# Check for NaN values in the entire DataFrame
nan_values = df.isna().sum()

# Alternatively, you can use df.isnull().sum()

# Print or use the information about NaN values
print(nan_values)

print(uniqueVal1)
print(uniqueVal3)
