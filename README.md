# Company Research Tool

A CLI tool that uses LangChain, OpenAI, and Tavily to research companies and fetch their logos and recent news articles.

## Architecture

### AI Components
- **LangChain**: Used as the orchestration framework to manage AI workflows and chain different operations together
- **OpenAI GPT**: Powers the natural language understanding and generation capabilities
- **Tavily**: Provides real-time news and information retrieval
- **Logo.dev**: Handles company logo retrieval and processing

### Prompt Engineering
The system uses a structured ReAct (Reasoning and Acting) prompt pattern that enables the AI to:
1. Analyze company information through a step-by-step reasoning process
2. Extract key insights from news articles
3. Generate a comprehensive company summary
4. Identify potential risks and opportunities

The ReAct pattern follows this structure:
- **Thought**: The AI reasons about what to do next
- **Action**: Selects an appropriate tool to use
- **Action Input**: Provides input to the selected tool
- **Observation**: Processes the tool's output
- This cycle repeats until the AI reaches a final answer

This approach ensures:
- Transparent decision-making process
- Iterative problem-solving
- Clear audit trail of the AI's reasoning
- Structured interaction with external tools

## Setup

1. Install Pipenv (if not already installed):
```bash
pip install pipenv
```

2. Activate the virtual environment:
```bash
pipenv shell
```

3. Install dependencies:
```bash
pipenv install
```


4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LOGO_API_KEY=your_logo_api_key_here (There's one already provided on .env.example)
```

You'll need to:
- Get an OpenAI API key from https://platform.openai.com/
- Get a Tavily API key from https://tavily.com/
- Get a Logo.dev API key from https://logo.dev

## Usage

You can run the script in two ways:

1. With command line argument:
```bash
pipenv run python src/main.py --company stripe.com
```

The script will:
1. Fetch the company's logo using Logo.dev
2. Get 3 to 5 recent news articles about the company using Tavily
3. Display the results in a formatted output

# Examples

## 1. Ubersuggest

### bash
```bash
python src/main.py --company ubersugggest
```

### Langsmith Tace
https://smith.langchain.com/public/edd9d4f8-0414-48b7-a9b4-fce6d18cabb4/r/

### Output
# Company Logo 
![ubersuggest.com logo](https://img.logo.dev/ubersuggest.com?token=pk_M-QGkO2LSr6vQL9S4_Ez-g)

# Company Info
- Company Name: Ubersuggest
- Website: [ubersuggest.com](https://ubersuggest.com)
- CEO: Max Cheprasov
- Parent Company: NP Digital

# Company Summary
Ubersuggest is a global SEO and content platform that provides insights into organic and paid traffic. Recently, Max Cheprasov has joined as its CEO.

# Recent News Articles
1. [Ubersuggest (@ubersuggest) • Instagram photos and videos](https://www.instagram.com/ubersuggest/?hl=en) - Announcement of Guillaume Lansiaux as the new Director of Engineering.
2. [Ubersuggest Announces New CEO Max Cheprasov - GlobeNewswire](https://www.globenewswire.com/news-release/2021/04/20/2213117/0/en/Ubersuggest-Announces-New-CEO-Max-Cheprasov.html) - Max Cheprasov joins as CEO.
3. [New Ubersuggest Update: Get Better Traffic Insights on Your Competitors - Neil Patel](https://neilpatel.com/blog/traffic-insights-on-competitors/) - Provides insights into paid traffic.


## 2. Notion.so

### bash
```bash
python src/main.py --company notion
```

### Langsmith Trace
https://smith.langchain.com/public/9de92940-c8f4-4f86-bb8a-c04842f6f416/r

### Output

Company: notion
# Company Logo 
![Notion Logo](https://img.logo.dev/notion.so?token=pk_M-QGkO2LSr6vQL9S4_Ez-g)

# Company Info
- Domain: notion.so

# Company Summary
Notion is a popular productivity and collaboration tool that offers a variety of features to help individuals and teams organize their work efficiently.

# Recent News Articles
1. [What's New – Notion](https://www.notion.com/releases)
2. [EVERYTHING Notion Launched in 2024 (MASSIVE UPDATES!)](https://www.youtube.com/watch?v=Fxi6OAApodY)
3. [8 NEW Notion Updates You Don't Want to Miss! (February 2025)](https://www.youtube.com/watch?v=KYRMObh2-R4&pp=0gcJCdgAo7VqN5tD)