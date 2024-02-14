# import nltk

# nltk.download('cmudict')
import pandas as pd
file_path = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/dp_dataset.tsv"

file_path2 = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset_final.tsv"

df = pd.read_csv(file_path, sep='\t')

df2  = pd.read_csv(file_path2, sep='\t')

# uniqueVal2 = df['Pattern Category'].nunique()
# print(uniqueVal2)

# # Check for NaN values in the entire DataFrame
# nan_values = df.isna().sum()

dark_pattern_counts = df['Pattern Category'].value_counts()

dark_pattern_counts2 = df2['Pattern Category'].value_counts()   



print(dark_pattern_counts)

print(dark_pattern_counts2)

# Alternatively, you can use df.isnull().sum()

# Print or use the information about NaN values
# print(nan_values)

# print(uniqueVal1)
# print(uniqueVal3)

# new_df = df[['text', 'Pattern Category']]
# new_df.to_csv('F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.csv',sep="\t", index=False)