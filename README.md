# 📈 AI Stock Sentiment Tracker (FinBERT + CUDA)

An end-to-end data pipeline that fetches financial news and uses a Deep Learning model (FinBERT) to analyze market sentiment, optimized for NVIDIA GPUs.

## 🚀 Features
* **Live News Ingestion:** Fetches real-time headlines via NewsAPI.
* **GPU Accelerated:** Optimized for NVIDIA GTX 1650 using CUDA via WSL2.
* **Financial AI:** Uses `finbert` to classify sentiment (Positive/Negative/Neutral).
* **Data Visualization:** Overlays sentiment results with actual stock price movements.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **ML Frameworks:** PyTorch, Transformers (FinBERT)
* **Hardware:** NVIDIA GTX 1650 (4GB VRAM)
* **Environment:** WSL2 (Ubuntu), VS Code

## 📊 How to Run
1. **Setup API Key:** Add your NewsAPI key to a `.env` file:
   `NEWS_API_KEY="your_key_here"`
2. **Fetch News:** `python3 news_fetcher.py`
3. **Analyze Sentiment:** `python3 sentiment_analyzer.py`
4. **Visualize:** `python3 visualizer.py`

## 📁 Project Structure
* `news_fetcher.py`: API integration.
* `sentiment_analyzer.py`: AI inference engine.
* `visualizer.py`: Data plotting script.
* `.gitignore`: Keeps API keys and venv out of GitHub.
