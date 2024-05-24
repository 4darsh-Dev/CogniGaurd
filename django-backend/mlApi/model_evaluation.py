import torch
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import pandas as pd
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Load pre-trained model
label_dict = {"Urgency": 0, "Not Dark Pattern": 1, "Scarcity": 2, "Misdirection": 3, "Social Proof": 4, "Obstruction": 5, "Sneaking": 6, "Forced Action": 7}
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=len(label_dict))

# Load fine-tuned weights
fine_tuned_model_path = "F:/backup-kali/codeFiles/projects/cognigaurd/fine_tuned_bert/finetuned_BERT_epoch_5.model"
model.load_state_dict(torch.load(fine_tuned_model_path, map_location=torch.device('cpu')))

# Preprocess the new text
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

# Function to map numeric label to dark pattern name
def get_dark_pattern_name(label):
    reverse_label_dict = {v: k for k, v in label_dict.items()}
    return reverse_label_dict[label]

def find_dark_pattern(text_predict):
    encoded_text = tokenizer.encode_plus(
        text_predict,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=256,
        return_tensors='pt'
    )

    # Making the predictions
    model.eval()

    with torch.no_grad():
        inputs = {
            'input_ids': encoded_text['input_ids'],
            'attention_mask': encoded_text['attention_mask']
        }
        outputs = model(**inputs)

    predictions = outputs.logits

    # Post-process the predictions
    probabilities = torch.nn.functional.softmax(predictions, dim=1)
    predicted_label = torch.argmax(probabilities, dim=1).item()

    return get_dark_pattern_name(predicted_label)


# Load the dataset
file_path = "F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/new_dp_dataset.tsv"
df = pd.read_csv(file_path, sep="\t")


# Sample data for evaluation
# sample_data = [
#     {"text": "Hurry only 5 items left in the cart ", "label": "Urgency"},
#     {"text": "Product Info", "label" : "Not Dark Pattern"},
#     {"text": "Someone from Norway purchased a Super FG Grater - 12x Faster - 15% OFF", "label": "Social Proof"},
#     {"text": "Sign In With Google ", "label": "Not Dark Pattern"},
#     {"text": "Shop All", "label": "Not Dark Pattern"},
#     {"text": "You can change your preference here Shop for Select an age", "label": "Not Dark Pattern"},
#     {"text": "45 ADDED TO BAG IN THE PAST 24 HOURS", "label": "Social Proof"},
#     {"text": "87% offers claimed. Hurry up!", "label": "Scarcity"},
#     {"text": "HURRY! £32.99 UK DELIVERY ENDS SOON", "label": "Urgency"},
#     {"text": "ONLY 3 LEFT", "label": "Scarcity"},
#     {"text": "8 items left", "label": "Scarcity"},
#     {"text": "19 people viewed this product per day", "label": "Social Proof"},
#     {"text": "I don't want to save money" , "label": "Misdirection"},
#     {"text": "When you join the PetPlus Plan, you are given the option to purchase your membership on an annual or monthly basis and you are automatically enrolled in our recurring billing program. You may cancel at any time by contacting our customer service team, but you will not be refunded for any unused days on your membership if you choose to cancel prior to the end of your billing cycle. You may cancel your PetPlus membership at any time without penalty if you have not utilized any of your PetPlus benefits (including discounts on products and/or services)" , "label": "Obstruction"},
#     {"text": "Shipping Insurance Remove Insurance" , "label": "Sneaking"},
#     {"text": "I would like to join Backstage Pass & agree to the Terms & Conditions & to receive emails & other promotional offers" , "label": "Forced Action"},

  		


#     # Add more samples as needed
# ]

# Record the start time
start_time = time.time()

# Lists to store true labels and predicted labels
true_labels = []
predicted_labels = []

# Use tqdm to create a progress bar
# Use tqdm to create a progress bar
for _, row in tqdm(df.iterrows(), desc="Evaluating", unit="sample", total=len(df)):
    text_to_predict = row['Title']
    true_label = row['Category']

    # Make prediction
    predicted_darkp = find_dark_pattern(text_to_predict)

    # Store true and predicted labels
    true_labels.append(true_label)
    predicted_labels.append(predicted_darkp)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Calculate accuracy
accuracy = accuracy_score(true_labels, predicted_labels)

# Calculate precision, recall, and f1-score
precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predicted_labels, average='weighted')

# Create a confusion matrix
# conf_matrix = confusion_matrix(true_labels, predicted_labels, labels=label_dict.values())
conf_matrix = confusion_matrix(true_labels, predicted_labels, labels=list(label_dict.keys()))


# Display results in a table
results_table = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Score": [accuracy, precision, recall, f1]
})

# Plot a colorful confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=label_dict.keys(), yticklabels=label_dict.keys())
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Plot the results table
plt.figure(figsize=(8, 4))
sns.barplot(x='Metric', y='Score', data=results_table, palette='viridis')
plt.title('Results Table')
plt.show()


print("Confusion Matrix:")
print(conf_matrix)

print("\nResults Table:")
print(results_table)

print(f"\nTotal Time Taken: {total_time:.2f} seconds")
