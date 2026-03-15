import pandas as pd
import yfinance as ticker
import matplotlib.pyplot as plt

def create_dashboard():
    # 1. Load your AI results
    results = pd.read_csv('results.csv')
    results['published_at'] = pd.to_datetime(results['published_at'])
    
    # 2. Get Stock Data from Yahoo Finance
    print("Fetching stock prices...")
    nvda = ticker.Ticker("NVDA")
    # Get 5 days of data with 1-hour intervals
    hist = nvda.history(period="5d", interval="1h")
    
    # 3. Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Stock Price
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Stock Price ($)', color='tab:blue')
    ax1.plot(hist.index, hist['Close'], color='tab:blue', label='NVDA Price')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Create a second axis for Sentiment
    ax2 = ax1.twinx()
    ax2.set_ylabel('Sentiment', color='tab:red')
    
    # Convert sentiment labels to numbers for plotting
    mapping = {'positive': 1, 'neutral': 0, 'negative': -1}
    results['score'] = results['sentiment'].map(mapping)
    
    ax2.scatter(results['published_at'], results['score'], color='tab:red', label='AI Sentiment')
    ax2.set_yticks([-1, 0, 1])
    ax2.set_yticklabels(['Negative', 'Neutral', 'Positive'])

    plt.title('NVIDIA: AI Sentiment vs Stock Price')
    plt.savefig('dashboard.png')
    print("Dashboard saved as dashboard.png!")
    plt.show()

if __name__ == "__main__":
    create_dashboard()