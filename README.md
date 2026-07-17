#  AI-Powered Topic Summarizer

An AI-powered Python application that generates concise summaries for any topic using the **OpenAI API** and **Wikipedia API**. The project supports two different modes for generating content and demonstrates how multiple APIs can work together in a simple AI pipeline.

---

##  Overview

This project allows users to enter any topic and choose between two modes:

- **Generic Mode** – Generates an explanation using the OpenAI API.
- **Search Mode** – Retrieves information from Wikipedia before generating a summarized response.

The final summary is automatically saved to a text file for future reference.

---

##  Features

-  AI-generated topic explanations using the OpenAI API
-  Wikipedia-based information retrieval
-  Automatic AI summarization
-  Save summaries to a text file
-  JSON response parsing and processing
-  Simple command-line interface

---

##  Tech Stack

- Python
- OpenAI API
- Wikipedia API
- JSON
- File Handling

---

## Project Workflow

```text
           User Inputs a Topic
                   │
                   ▼
        Select Processing Mode
         ┌─────────┴─────────┐
         ▼                   ▼
 Generic Mode          Search Mode
(OpenAI API)      (Wikipedia API)
         │                   │
         └─────────┬─────────┘
                   ▼
         AI Generates Summary
                   │
                   ▼
         Save Output to File
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Topic-Summarizer.git
```

### 2. Navigate to the project

```bash
cd AI-Topic-Summarizer
```

### 4. Create a `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

---

### Usage

Run the project:

```bash
python main.py
```

Example:

```text
Enter a topic:
Artificial Intelligence

Choose a mode:
1. Generic Mode
2. Search Mode

Your Choice: 2
```

The application will generate a summary and save it to `summary.txt`.

---

## 📚 What I Learned

- Working with REST APIs in Python
- Integrating the OpenAI API
- Fetching data using the Wikipedia API
- Parsing and processing JSON responses
- Building a simple AI pipeline
- Managing data flow between multiple services
- Saving generated output to files

---

##  Future Improvements

- GUI 
- PDF export support
- Voice input and text-to-speech
- Chat history management
  
---

### Author 

Javairia Lateef

---
