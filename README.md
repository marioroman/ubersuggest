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

2. Install dependencies:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LOGO_API_KEY=your_logo_api_key_here
```

You'll need to:
- Get an OpenAI API key from https://platform.openai.com/
- Get a Tavily API key from https://tavily.com/
- Get a Logo.dev API key from https://logo.dev

## Building the Application

1. Clone the repository:
```bash
git clone <repository-url>
cd company-research-tool
```

2. Install development dependencies:
```bash
pipenv install --dev
```

3. Run tests:
```bash
pipenv run pytest
```

4. Build the package:
```bash
pipenv run python setup.py build
```

5. Install the package locally:
```bash
pipenv install -e .
```

## Usage

You can run the script in two ways:

1. With command line argument:
```bash
pipenv run python src/main.py --company stripe.com
```

2. Interactive mode (if no argument is provided):
```bash
pipenv run python src/main.py
```

The script will:
1. Fetch the company's logo using Logo.dev
2. Get 3 recent news articles about the company using Tavily
3. Display the results in a formatted output

## Future Improvements

### Phase 2 Enhancements

1. **Enhanced AI Capabilities**
   - Implement sentiment analysis for news articles
   - Add competitor analysis using AI
   - Integrate financial data analysis
   - Add trend prediction capabilities

2. **User Experience**
   - Add a web interface
   - Implement batch processing for multiple companies
   - Add export functionality (PDF, CSV, JSON)
   - Create customizable report templates

3. **Data Integration**
   - Add more data sources (e.g., Crunchbase, LinkedIn)
   - Implement real-time data updates
   - Add historical data analysis
   - Create data visualization dashboards

4. **Performance & Scalability**
   - Implement caching for frequently accessed data
   - Add rate limiting and error handling
   - Optimize API calls and reduce latency
   - Add support for concurrent processing

5. **Security & Compliance**
   - Implement user authentication
   - Add data encryption
   - Ensure GDPR compliance
   - Add audit logging 


# Examples

## 1. Ubersuggest

```bash
python src/main.py --company ubersugggest
```

Company: ubersugggest
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
```bash
python src/main.py --company notion
```

Company: notion
# Company Logo 
![notion.so logo](https://img.logo.dev/notion.so?token=pk_M-QGkO2LSr6vQL9S4_Ez-g)

# Company Info
- Domain: [notion.so](https://www.notion.so)
- Recent News: 
    - [Notion in the News](https://uno.notion.vip/insights/notion-in-the-news/)
    - [What's New – Notion](https://www.notion.com/releases)
    - [9 New Notion Updates (in under 14 minutes) - April 2025 - YouTube](https://www.youtube.com/watch?v=DxUzkC58ZQQ)

# Company Summary
Notion is a collaboration software company that has recently reached a $10 billion valuation. They have been expanding globally and have made significant updates to their platform, including removing limits on their free plan and raising $50 million in funding.

# Relevant Articles
1. [Notion in the News](https://uno.notion.vip/insights/notion-in-the-news/)
2. [What's New – Notion](https://www.notion.com/releases)
3. [9 New Notion Updates (in under 14 minutes) - April 2025 - YouTube](https://www.youtube.com/watch?v=DxUzkC58ZQQ)