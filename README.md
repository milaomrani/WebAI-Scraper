# WebAI-Scraper

## Overview
**WebAI-Scraper** is a web scraping and data analysis tool designed to gather and analyze information about AI applications in the agricultural sector. The tool employs a multi-agent architecture powered by `requests`, `BeautifulSoup`, and `LangChain` with a local LLM from Ollama.

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
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/WebAI-Scraper.git
    cd AgriAI-Scraper
    ```
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Ensure that the Ollama LLM is installed and running locally.

## Usage
1. Set up the `search_and_scrape` function to initiate a search and scrape process. Modify the query to your interest.
2. Define agents for scraping, analyzing, and summarizing the collected data.
3. Run the crew to kick off the tasks:
    ```python
    result = ai_agri_crew.kickoff()
    print(result)
    ```

## Example
You can run the script to search for the latest AI innovations in agriculture and generate a summary of the top companies and trends:
```python
query = "AI applications in agriculture"
result = search_and_scrape(query)
print(result)
