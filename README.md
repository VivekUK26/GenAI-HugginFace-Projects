GenAI Applications using Hugging Face Models
This repository contains four Generative AI applications built using Hugging Face Transformers and Gradio interfaces. Each project demonstrates different capabilities of modern language models for practical use cases.

Projects Overview

1.Text Summarizer
A simple text summarization application that uses the DistilBART-CNN model to generate concise summaries of input text.
Features:
Uses sshleifer/distilbart-cnn-12-6 model
Gradio interface for easy interaction
Supports multi-line text input
Optimized with torch.bfloat16 for better performance



2.YouTube Script Summarizer
An application that extracts and summarizes YouTube video transcripts using the DistilBART-CNN model.
Features:
Automatic YouTube video ID extraction from URLs
Supports multiple YouTube URL formats
Transcript extraction using youtube_transcript_api
Text summarization using DistilBART-CNN
User-friendly Gradio interface




3.Document Q&A
A question-answering system built using RoBERTa model that answers questions based on provided document context.
Features:
Uses deepset/roberta-base-squad2 model
File upload support for context documents
Direct question input through Gradio interface
Efficient answer extraction from context




4.Sentiment Analyzer
A bulk sentiment analysis system for processing customer reviews using DistilBERT model.
Features:
Uses distilbert-base-uncased-finetuned-sst-2-english model
Excel file processing support
Visual sentiment distribution through pie charts
Batch processing capabilities
Interactive data visualization
Professional Gradio interface
