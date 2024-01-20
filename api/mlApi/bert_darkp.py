import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import pandas as pd

# Load your dataset and preprocess it
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path, sep='\t')
    return df[['text', 'label', 'Pattern Category']]

# Tokenize the data for binary classification
def tokenize_binary_data(data, tokenizer):
    tokens = tokenizer.batch_encode_plus(
        data['text'].tolist(),
        padding=True,
        truncation=True,
        return_tensors='pt'
    )
    return TensorDataset(tokens['input_ids'], tokens['attention_mask'], torch.tensor(data['label'].tolist()))

# Tokenize the data for multiclass classification
def tokenize_multiclass_data(data, tokenizer):
    tokens = tokenizer.batch_encode_plus(
        data['text'].tolist(),
        padding=True,
        truncation=True,
        return_tensors='pt'
    )
    return TensorDataset(tokens['input_ids'], tokens['attention_mask'], torch.tensor(data['Pattern Category'].astype(int).tolist()))

# Fine-tune BERT model for binary classification with tqdm progress bar
def fine_tune_binary_bert_model(model, dataloader, optimizer, num_epochs=3):
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0.0
        progress_bar = tqdm(dataloader, desc=f'Epoch {epoch + 1}/{num_epochs}', leave=False)

        for batch in progress_bar:
            optimizer.zero_grad()
            outputs = model(batch[0], attention_mask=batch[1], labels=batch[2])
            loss = outputs.loss
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            progress_bar.set_postfix({'Loss': total_loss / len(progress_bar)})

        progress_bar.close()

# Fine-tune BERT model for multiclass classification with tqdm progress bar
def fine_tune_multiclass_bert_model(model, dataloader, optimizer, num_epochs=3):
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0.0
        progress_bar = tqdm(dataloader, desc=f'Epoch {epoch + 1}/{num_epochs}', leave=False)

        for batch in progress_bar:
            optimizer.zero_grad()
            outputs = model(batch[0], attention_mask=batch[1], labels=batch[2])
            loss = outputs.loss
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            progress_bar.set_postfix({'Loss': total_loss / len(progress_bar)})

        progress_bar.close()

# Save the fine-tuned models
def save_models(binary_model, multiclass_model, tokenizer, output_dir='fine_tuned_models'):
    binary_model.save_pretrained(output_dir + '/binary_model')
    multiclass_model.save_pretrained(output_dir + '/multiclass_model')
    tokenizer.save_pretrained(output_dir)

# Load the fine-tuned models
def load_models(output_dir='fine_tuned_models'):
    binary_model = BertForSequenceClassification.from_pretrained(output_dir + '/binary_model', num_labels=2)
    multiclass_model = BertForSequenceClassification.from_pretrained(output_dir + '/multiclass_model', num_labels=num_categories)
    tokenizer = BertTokenizer.from_pretrained(output_dir)
    return binary_model, multiclass_model, tokenizer

# Example usage:
file_path = 'F:/backup-kali/codeFiles/projects/cognigaurd/api/datasets/dataset.tsv'
data = load_and_preprocess_data(file_path)

# Binary classification
binary_labels = data['label'].apply(lambda x: 1 if x == 1 else 0)
data['binary_label'] = binary_labels

# Split the dataset
train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

# Tokenize data for binary classification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
train_binary_dataset = tokenize_binary_data(train_data, tokenizer)
val_binary_dataset = tokenize_binary_data(val_data, tokenizer)

# Create DataLoader
train_binary_dataloader = DataLoader(train_binary_dataset, batch_size=8, shuffle=True)
val_binary_dataloader = DataLoader(val_binary_dataset, batch_size=8, shuffle=False)

# Fine-tune binary classification model
binary_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
optimizer = torch.optim.AdamW(binary_model.parameters(), lr=2e-5)

fine_tune_binary_bert_model(binary_model, train_binary_dataloader, optimizer)

# Multiclass classification
num_categories = data['Pattern Category'].nunique()

# Tokenize data for multiclass classification
train_multiclass_dataset = tokenize_multiclass_data(train_data, tokenizer)
val_multiclass_dataset = tokenize_multiclass_data(val_data, tokenizer)

# Create DataLoader
train_multiclass_dataloader = DataLoader(train_multiclass_dataset, batch_size=8, shuffle=True)
val_multiclass_dataloader = DataLoader(val_multiclass_dataset, batch_size=8, shuffle=False)

# Fine-tune multiclass classification model
multiclass_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=num_categories)
optimizer = torch.optim.AdamW(multiclass_model.parameters(), lr=2e-5)

fine_tune_multiclass_bert_model(multiclass_model, train_multiclass_dataloader, optimizer)

# Save the models
save_models(binary_model, multiclass_model, tokenizer)

# For inference:
# Load the models
loaded_binary_model, loaded_multiclass_model, loaded_tokenizer = load_models()

# Tokenize new text for binary classification
new_text = "Your random text here."
new_tokens_binary = loaded_tokenizer.batch_encode_plus([new_text], padding=True, truncation=True, return_tensors='pt')
new_binary_input = TensorDataset(new_tokens_binary['input_ids'], new_tokens_binary['attention_mask'])

# Tokenize new text for multiclass classification
new_tokens_multiclass = loaded_tokenizer.batch_encode_plus([new_text], padding=True, truncation=True, return_tensors='pt')
new_multiclass_input = TensorDataset(new_tokens_multiclass['input_ids'], new_tokens_multiclass['attention_mask'])

# Inference for binary classification
binary_model.eval()
with torch.no_grad():
    binary_outputs = binary_model(new_binary_input[0], attention_mask=new_binary_input[1])
    binary_prediction = torch.argmax(binary_outputs.logits, dim=1).item()

# Inference for multiclass classification
multiclass_model.eval()
with torch.no_grad():
    multiclass_outputs = multiclass_model(new_multiclass_input[0], attention_mask=new_multiclass_input[1])
    multiclass_prediction = torch.argmax(multiclass_outputs.logits, dim=1).item()

# Output
print(f"Dark Pattern Presence (Binary Classification): {binary_prediction}")
print(f"Dark Pattern Category (Multiclass Classification): {multiclass_prediction}")
