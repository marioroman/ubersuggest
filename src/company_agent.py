import os
from typing import Dict, List
import requests
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

class CompanyResearchAgent:
    def __init__(self):
        # Check if required API keys are set
        if not all([
            os.getenv("OPENAI_API_KEY"),
            os.getenv("TAVILY_API_KEY"),
            os.getenv("LOGO_DEV_API_KEY")
        ]):
            raise ValueError("Missing required API keys. Please check your .env file.")
            
        # Initialize Tavily client
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        # Initialize tools
        self.tools = [
            Tool(
                name="get_company_logo",
                func=self.get_company_logo,
                description="""Get company logo from LogoDev. Input must be a company domain (e.g. 'google.com' or 'https://google.com').
                    The domain should be the company's website address, not just the company name."""
            ),
            Tool(
                name="get_company_news",
                func=self.get_company_news,
                description="Get recent news articles about the company."
            )
        ]
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            temperature=0,
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY")
        )
        
        # Initialize agent
        self.agent = self._create_agent()
        
    def get_company_logo(self, domain: str) -> str:
        """Get company logo from logo.dev
        
        Args:
            domain (str): Company domain (e.g. 'google.com' or 'https://google.com')
            
        Returns:
            str: Markdown image syntax if logo is found, error message if not found
        """
        try:
            # Remove http/https and www if present
            domain = domain.replace("https://", "").replace("http://", "").replace("www.", "")
            
            # Construct logo.dev URL
            logo_url = f"https://img.logo.dev/{domain}?token={os.getenv('LOGO_DEV_API_KEY')}"
            
            # Set proper headers
            headers = {
                'Accept': 'image/*',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Make request to verify logo exists
            response = requests.head(logo_url, headers=headers, allow_redirects=True)
            
            # Try GET request if HEAD fails
            if response.status_code != 200:
                response = requests.get(logo_url, headers=headers)
            
            if response.status_code == 200:
                return f"![{domain} logo]({logo_url})"
            return f"Logo not found for {logo_url} response: {response.status_code}"
        except Exception as e:
            return f"Error fetching logo: {str(e)}"

    
    def get_company_news(self, company: str) -> List[Dict]:
        """Get recent news articles about the company using Tavily"""
        try:
            search_result = self.tavily_client.search(
                query=f"latest news about {company}",
                search_depth="advanced",
                max_results=3,
                search_type="news",
                sort_by="relevance"
            )
            return search_result.get('results', [])
        except Exception as e:
            return [{"error": f"Error fetching news: {str(e)}"}]
    
    def _create_agent(self) -> AgentExecutor:
        """Create and return the agent executor"""
        prompt = PromptTemplate.from_template(
            """You are a company research assistant. Use the following tools to gather information about the company:

            {tools}

            Use the following format:
            Question: the input question you must answer
            Thought: you should always think about what to do
            Action: the action to take, should be one of [{tool_names}]
            Action Input: the input to the action
            Observation: the result of the action
            ... (this Thought/Action/Action Input/Observation can repeat N times)
            Thought: I now know the final answer
            Final Answer: the final answer to the original input question

            Question: {input}
            {agent_scratchpad}"""
        )
        
        agent = create_react_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=prompt
        )
        
        return AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )
    
    def research_company(self, company: str) -> Dict:
        """Research a company and return the results"""
        try:
            # Use the agent to research the company
            result = self.agent.invoke({
                "input": f"""Research the company {company}. 
                1. Get company domain 
                2. Get their logo, company info, 
                3. and a company summary.
                4. Include recent news articles.

                With that information create a markdown report with the following elenments and sections:

                # Company Logo 
                (logo as a markdown image icon)
                # Company Info (as a markdown list)
                # Company Summary
                # Between 3 to 5 company most relevant articles. Links to the articles should be included.

                If no information is available, just return "No information found"
                """
            })
            
            # Parse the agent's response
            if "error" in result:
                return {"Something went wrong parsing the response": result["error"]}
                
            # Extract information from the agent's response
            return {
                "company": company,
                "agent_response": result["output"]
            }
        except Exception as e:
            return {"Something went wrong": str(e)} 