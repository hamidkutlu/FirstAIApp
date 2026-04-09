# Tweet Generator

A Streamlit web application that generates tweets on any topic using Google's Gemini AI model, orchestrated with LangChain.

## Features

- Generate 1 to 10 tweets on any user-specified topic
- Powered by Google's Gemini 1.5 Flash model for fast, high-quality text generation
- Simple, interactive web UI built with Streamlit
- LangChain integration for clean prompt templating and model chaining

## Tech Stack

- **[Streamlit](https://streamlit.io/)** - Web UI framework
- **[LangChain](https://www.langchain.com/)** - LLM orchestration and prompt management
- **[Google Generative AI (Gemini)](https://ai.google.dev/)** - Large language model for tweet generation

## Setup

### Prerequisites

- Python 3.8+
- A Google API key with access to the Gemini API

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/satvik314/basic_app_template.git
   cd basic_app_template
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Google API key using Streamlit secrets. Create a `.streamlit/secrets.toml` file:
   ```toml
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```

### Running the App

```bash
streamlit run main.py
```

## Usage

1. Enter a topic in the text input field (e.g., "artificial intelligence", "climate change")
2. Select the number of tweets to generate (1-10)
3. Click the **Generate** button
4. View the generated tweets displayed on the page

## Project Structure

```
basic_app_template/
├── main.py              # Main Streamlit application with LangChain + Gemini integration
├── requirements.txt     # Python package dependencies
├── .gitignore           # Git ignore rules for Python projects
└── README.md            # Project documentation
```
