# import nltk

# nltk.download('cmudict')
import pandas as pd
file_path = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.tsv"

file_path2 = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.csv"

file_path3 = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/dp_final_dataset_may_4k.csv"


df = pd.read_csv(file_path, sep='\t')

df2  = pd.read_csv(file_path2)

df3 = pd.read_csv(file_path3)

# uniqueVal2 = df['Pattern Category'].nunique()
# print(uniqueVal2)

# # Check for NaN values in the entire DataFrame
# nan_values = df.isna().sum()

dark_pattern_counts = df['Category'].value_counts()

dark_pattern_counts2 = df2['Category'].value_counts()   

dark_pattern_counts3 = df3['Category'].value_counts()




# print(dark_pattern_counts)

# print(dark_pattern_counts2)

print(dark_pattern_counts3)

# Alternatively, you can use df.isnull().sum()

# Print or use the information about NaN values
# print(nan_values)

# print(uniqueVal1)
# print(uniqueVal3)

# new_df = df[['text', 'Pattern Category']]
# new_df.to_csv('F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.csv',sep="\t", index=False)


# import pandas as pd

# output_file_path = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.csv"

# # Read the TSV file
# df = pd.read_csv(file_path2, sep='\t')

# # Write the DataFrame to a CSV file
# df.to_csv(output_file_path, index=False)

# print("TSV file converted to CSV successfully!")

# df3 = pd.read_csv(output_file_path)
# dark_pattern_counts3 = df3['Category'].value_counts()
# print(dark_pattern_counts3)


##3 checking for incosistency in dataset


import csv

def check_class_sizes(filename, encoding='utf-8'):
    # Dictionary to store class sizes
    class_sizes = {}
    row_count = 0  # Counter for row numbers

    # Read the CSV file with the specified encoding
    with open(filename, 'r', encoding=encoding) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        # Iterate through each row in the CSV file
        for row in reader:
            row_count += 1  # Increment row counter

            if len(row) != 2:
                print(f"Warning: Skipping row {row_count} with incorrect number of values: {row}")
                continue
            title, category = row

            # Update the class size count
            if category in class_sizes:
                class_sizes[category] += 1
            else:
                class_sizes[category] = 1

    # Check for classes with only one member
    for category, size in class_sizes.items():
        if size == 1:
            print(f"Warning: The class '{category}' has only one member.")

    return class_sizes

# Example usage
filename = file_path3
encoding = 'utf-8'  # You can change the encoding as needed
class_sizes = check_class_sizes(filename, encoding)
print("Class sizes:", class_sizes)

