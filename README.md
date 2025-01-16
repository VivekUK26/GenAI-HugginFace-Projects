GenAI Applications using Hugging Face Models

This repository contains three Generative AI applications built using Hugging Face Transformers and Gradio interfaces. Each project demonstrates different capabilities of modern language models for practical use cases.
Projects Overview
1. Text Summarizer
  A simple text summarization application that uses the DistilBART-CNN model to generate concise summaries of input text.
  Features:
    Uses sshleifer/distilbart-cnn-12-6 model
    Gradio interface for easy interaction
    Supports multi-line text input
    Optimized with torch.bfloat16 for better performance

2. YouTube Script Summarizer
  An application that extracts and summarizes YouTube video transcripts using the DistilBART-CNN model.
  Features:
    Automatic YouTube video ID extraction from URLs
    Supports multiple YouTube URL formats
    Transcript extraction using youtube_transcript_api
    Text summarization using DistilBART-CNN
    User-friendly Gradio interface
3. Document Q&A
  A question-answering system built using RoBERTa model that answers questions based on provided document context.
  Features:
    Uses deepset/roberta-base-squad2 model
    File upload support for context documents
    Direct question input through Gradio interface
    Efficient answer extraction from context

Installation

Clone the repository:
git clone https://github.com/VivekUK26/GenAI-HugginFace-Projects.git
cd GenAI-HugginFace-Projects

Install required packages:
pip install torch transformers gradio youtube_transcript_api

Usage
Text Summarizer
python textsummary.py

  Enter your text in the input box
  Click submit to generate the summary

YouTube Summarizer
python YouTubeSummerizer.py

  Paste a YouTube URL in the input box
  Click submit to get the video transcript summary

Document Q&A
python document_qna.py

  Upload a text file containing the context
  Enter your question
  Click submit to get the answer

Project Structure
GenAI-HugginFace-Projects/
├── textsummary.py
├── YouTubeSummerizer.py
├── document_qna.py
└── README.md

Dependencies
  Python 3.7+
  PyTorch
  Transformers
  Gradio
  youtube_transcript_api

Models Used
  DistilBART-CNN: sshleifer/distilbart-cnn-12-6
  RoBERTa: deepset/roberta-base-squad2

Contributing
Feel free to open issues or submit pull requests for improvements.
