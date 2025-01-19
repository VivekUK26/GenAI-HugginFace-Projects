import torch
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Initialize sentiment analysis model
analyzer = pipeline("text-classification",
                    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analyzer(review):
    """Analyze sentiment of a single review."""
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_bar_chart(df):
    """Generate pie chart visualization of sentiment distribution."""
    sentiment_counts = df['Sentiment'].value_counts()

    fig, ax = plt.subplots()
    sentiment_counts.plot(
        kind='pie',
        ax=ax,
        autopct='%1.1f%%',
        color=['green', 'red']
    )
    ax.set_title('Review Sentiment Counts')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')

    return fig


def read_reviews_and_analyze_sentiment(file_object):
    """Process Excel file and analyze sentiments."""
    # Load and validate Excel file
    df = pd.read_excel(file_object)
    if 'Reviews' not in df.columns:
        raise ValueError("Excel file must contain a 'Review' column.")

    # Analyze sentiments and generate visualization
    df['Sentiment'] = df['Reviews'].apply(sentiment_analyzer)
    chart_object = sentiment_bar_chart(df)

    return df, chart_object


# Create Gradio interface
demo = gr.Interface(
    fn=read_reviews_and_analyze_sentiment,
    inputs=[gr.File(
        file_types=["xlsx"],
        label="Upload your review comment file"
    )],
    outputs=[
        gr.Dataframe(label="Sentiments"),
        gr.Plot(label="Sentiment Analysis")
    ],
    title="Gen AI Project 3: Sentiment Analyzer",
    description="THIS APPLICATION WILL BE USED TO ANALYZE THE SENTIMENT BASED ON FILE UPLOADED."
)

# Launch the application
if __name__ == "__main__":
    demo.launch()