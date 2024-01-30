import torch
from transformers import BertTokenizer, BertForSequenceClassification
from tqdm import tqdm  # Import tqdm for progress bar

import time # for time taken calc

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

# text_to_predict = "Hello my name is adarsh and my friend name is aman , he is only on sale for the next two days. "

text_to_predict = "Hurry only 5 items left otherwise they will be sold out. "

# Record the start time
start_time = time.time()

# Add a simple progress message
print("Predicting Dark Pattern...")

# Use tqdm to create a progress bar
for _ in tqdm(range(10), desc="Predicting", unit="prediction"):
    predicted_darkp = find_dark_pattern(text_to_predict)

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

print(f"Predicted Dark Pattern: {predicted_darkp}")
print(f"Total Time Taken: {total_time:.2f} seconds")
