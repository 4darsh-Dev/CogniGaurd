import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from termsMlModel import load_dataset, preprocess_data, train_model, evaluate_model

# Task 1: Load your dataset
dataset_path = 'path/to/your_dataset.csv'  # Replace with the path to your dataset
texts, labels = load_dataset(dataset_path)

# Task 2: Configure model parameters
model_name = 'bert-base-uncased'
num_labels = 2  # Binary classification (dark pattern or not)
batch_size = 8
max_length = 512  # Adjust based on your dataset and model's input size

# Task 3: Preprocess the data
# Split the dataset
texts_train, texts_val, labels_train, labels_val = train_test_split(texts, labels, test_size=0.1, random_state=42)

# Preprocess the training data
train_dataset = preprocess_data(texts_train, labels_train, max_length)
train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Preprocess the validation data
val_dataset = preprocess_data(texts_val, labels_val, max_length)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Set up the BERT model
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

# Train the model
epochs = 3
learning_rate = 2e-5
train_model(model, train_dataloader, val_dataloader, epochs, learning_rate)

# Evaluate the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
evaluate_model(model, val_dataloader, device)
