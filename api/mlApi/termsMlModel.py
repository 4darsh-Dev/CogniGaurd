import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_dataset(dataset_path):
    # Replace this with your actual dataset loading code
    import pandas as pd
    df = pd.read_csv(dataset_path)
    texts = df['text'].tolist()
    labels = df['label'].tolist()
    return texts, labels

def preprocess_data(texts, labels, max_length):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    encodings = tokenizer(texts, truncation=True, padding='max_length', max_length=max_length, return_tensors='pt')
    dataset = DarkPatternDataset(encodings['input_ids'], encodings['attention_mask'], torch.tensor(labels))
    return dataset

def train_model(model, train_dataloader, val_dataloader, epochs, learning_rate):
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    total_steps = len(train_dataloader) * epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.train()

    for epoch in range(epochs):
        for batch in train_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            scheduler.step()

def evaluate_model(model, val_dataloader, device='cpu'):
    model.eval()
    val_predictions = []
    val_true_labels = []

    with torch.no_grad():
        for batch in val_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=1).cpu().numpy()

            val_predictions.extend(predictions)
            val_true_labels.extend(labels.cpu().numpy())

    accuracy = accuracy_score(val_true_labels, val_predictions)
    print(f'Validation Accuracy: {accuracy * 100:.2f}%')

class DarkPatternDataset(Dataset):
    def __init__(self, input_ids, attention_mask, labels):
        self.input_ids = input_ids
        self.attention_mask = attention_mask
        self.labels = labels

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {'input_ids': self.input_ids[idx].squeeze(), 'attention_mask': self.attention_mask[idx].squeeze(), 'labels': self.labels[idx]}
