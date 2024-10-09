import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task, Crew
from langchain.tools import Tool
from langchain.llms import Ollama
import time

def search_and_scrape(query, max_pages=10):
    base_url = "https://duckduckgo.com/html/"
    params = {'q': query, 's': '0', 'dc': ''}
    all_results = []

    for page in range(max_pages):
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='result__body')
        
        if not results:
            break  # No more results found
        
        all_results.extend(results)
        
        # Update parameters for the next page
        next_link = soup.find('a', class_='nav-link', attrs={'data-nir': ''})
        if not next_link:
            break  # No more pages
        
        params['s'] = next_link.get('href').split('s=')[1].split('&')[0]
        params['dc'] = str(int(params['dc']) + 1) if params['dc'] else '1'
        
        time.sleep(1)  # Be respectful to the server

    return "\n\n".join([result.text.strip() for result in all_results])

# Set up the local LLM using Ollama
# llm = Ollama(model="llama3.1:latest")  # You can change the model as needed
llm = LLM(model="ollama/llama3.1:latest", base_url="http://localhost:11434")


# Wrap the function in a Tool object
search_tool = Tool(
    name="Web Search",
    func=search_and_scrape,
    description="Searches the web for information about a given query, looking through up to 10 pages of results"
)

# Define agents
web_scraper = Agent(
    role="Web Scraper",
    goal="Gather comprehensive information about AI in agriculture from the internet",
    backstory="You are an expert web scraper with a focus on agricultural technology. You're thorough and can analyze multiple pages of search results.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

analyzer = Agent(
    role="Data Analyzer",
    goal="Analyze the gathered information and identify key trends, companies, and innovations",
    backstory="You are a data analyst specializing in agricultural technology trends. You can process large amounts of information and extract meaningful insights.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

summarizer = Agent(
    role="Content Summarizer",
    goal="Create concise yet comprehensive summaries of the analyzed information",
    backstory="You are an expert in distilling complex information into clear, concise summaries. You can handle large volumes of data and extract the most important points.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define tasks
task_scrape = Task(
    description="Search for and gather information about AI applications in agriculture, focusing on company activities and innovations. Look through up to 10 pages of search results for a comprehensive overview.",
    agent=web_scraper,
    expected_output="A comprehensive list of search results about AI in agriculture from up to 10 pages of search results"
)

task_analyze = Task(
    description="Analyze the gathered information to identify key companies, trends, and innovations in AI for agriculture. Consider the breadth of information from multiple search result pages.",
    agent=analyzer,
    expected_output="A detailed analysis of key companies, trends, and innovations in AI for agriculture based on comprehensive search results"
)

task_summarize = Task(
    description="Create a concise yet comprehensive summary of the top companies using AI in agriculture, their main applications, and notable trends. Ensure the summary reflects the breadth of information gathered from multiple search result pages.",
    agent=summarizer,
    expected_output="A comprehensive summary of top companies, applications, and trends in AI for agriculture, reflecting insights from multiple pages of search results"
)

# Create the crew
ai_agri_crew = Crew(
    agents=[web_scraper, analyzer, summarizer],
    tasks=[task_scrape, task_analyze, task_summarize],
    verbose=True
)

# Run the crew
result = ai_agri_crew.kickoff()
print(result)
