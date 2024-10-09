# WebAI-Scraper

## Overview
**AgriAI-Scraper** is a web scraping and data analysis tool designed to gather and analyze information about AI applications in the agricultural sector. The tool employs a multi-agent architecture powered by `requests`, `BeautifulSoup`, and `LangChain` with a local LLM from Ollama.

## Features
- **Web Scraping**: Scrapes up to 10 pages of search results for a given query using DuckDuckGo.
- **Data Analysis**: Analyzes the gathered information to extract key trends, companies, and innovations.
- **Summarization**: Provides concise summaries of top AI applications in agriculture.
  
## Tech Stack
- **requests**: For sending HTTP requests to search engines.
- **BeautifulSoup**: For parsing and scraping web data.
- **LangChain**: To manage agents and tasks.
- **Ollama LLM**: Used for language modeling and generating insights.
  
## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/milaomrani/WebAI-Scraper.git
cd webAI-Scraper
```

### 2. Install required Python packages:
```bash
pip install -r requirements.txt
```


### 3. Install and set up Ollama LLM:
Download and install Ollama LLM from here.
Start the Ollama server locally:
```
ollama serve
```

Confirm Ollama is running by checking localhost:11434 or by running:
```
ollama list
```
Ensure Ollama is set up to use the correct model:
```
ollama pull llama3.1:latest
```
Usage
Running the Script in Terminal
Set up the search_and_scrape function with your query, for example:
```
python run.py --query "AI applications in agriculture"
```
