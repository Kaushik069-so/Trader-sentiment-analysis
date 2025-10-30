from data_preprocessing import load_and_merge_data
from visualization import plot_sentiment_trends, plot_performance_by_sentiment, plot_leverage_distribution

if __name__ == "__main__":
    print("📊 Loading and merging data...")
    merged_data = load_and_merge_data(
        "data/fear_greed_index.csv",
        "data/compressed_data.csv.gz"
    )

    print("📈 Generating insights and visualizations...")
    plot_sentiment_trends(merged_data)
    plot_performance_by_sentiment(merged_data)
    plot_leverage_distribution(merged_data)

    print("✅ All graphs saved to 'results/' folder.")
