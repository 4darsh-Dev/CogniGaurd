from transformers import  TFAutoModel, AutoTokenizer

# loading model
model = TFAutoModel.from_pretrained("bert-base-uncased")

#loading tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello, my dog is cute", return_tensors="tf", padding=True, truncation=True)

print(inputs)

output = model(input)
print(output)