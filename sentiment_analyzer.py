import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def run_analysis():
    df = pd.read_csv('news_data.csv')
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")
    
    # Load FinBERT
    model_name = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
    
    def predict(text):
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64).to(device)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        val, idx = torch.max(probs, dim=1)
        return ['positive', 'negative', 'neutral'][idx.item()]

    print("AI is analyzing headlines...")
    df['sentiment'] = df['title'].apply(predict)
    df.to_csv('results.csv', index=False)
    print("Success! Results saved to results.csv")
    print(df.head())

if __name__ == "__main__":
    run_analysis()