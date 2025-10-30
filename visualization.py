import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("results", exist_ok=True)

def plot_sentiment_trends(data):
    trend = data.groupby('Classification').size()
    trend.plot(kind='bar', color=['orange', 'green'])
    plt.title("Market Sentiment Distribution (Fear vs Greed)")
    plt.ylabel("Number of Days")
    plt.savefig("results/sentiment_trend.png")
    plt.close()

def plot_performance_by_sentiment(data):
    avg_pnl = data.groupby('Classification')['closedPnL'].mean().reset_index()
    sns.barplot(x='Classification', y='closedPnL', data=avg_pnl, palette='coolwarm')
    plt.title("Average Trader Performance by Sentiment")
    plt.ylabel("Average Closed PnL")
    plt.savefig("results/avg_pnl_by_sentiment.png")
    plt.close()

def plot_leverage_distribution(data):
    sns.boxplot(x='Classification', y='leverage', data=data, palette='Set2')
    plt.title("Leverage Distribution by Market Sentiment")
    plt.ylabel("Leverage")
    plt.savefig("results/leverage_distribution.png")
    plt.close()
