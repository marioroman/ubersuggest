import os
import logging
from typing import Dict, List
import requests
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langsmith import Client
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks.manager import CallbackManager

logger = logging.getLogger(__name__)

class CompanyResearchAgent:
    def __init__(self):
        # Check if required API keys are set
        if not all([
            os.getenv("OPENAI_API_KEY"),
            os.getenv("TAVILY_API_KEY"),
            os.getenv("LOGO_DEV_API_KEY")
        ]):
            logger.error("Missing required API keys")
            raise ValueError("Missing required API keys. Please check your .env file.")
            
        # Initialize LangSmith client if API key is available
        self.langsmith_client = None
        if os.getenv("LANGSMITH_API_KEY"):
            self.langsmith_client = Client()
            logger.debug("LangSmith client initialized")
            
        # Initialize Tavily client
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        logger.debug("Tavily client initialized")
        
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
        logger.debug("Tools initialized")
        
        # Initialize LLM with LangSmith tracing if available
        callback_manager = None
        if os.getenv("LANGCHAIN_API_KEY"):
            tracer = LangChainTracer()
            callback_manager = CallbackManager([tracer])
            logger.debug("LangChain tracer initialized")
            
        self.llm = ChatOpenAI(
            temperature=0,
            model="gpt-3.5-turbo",
            api_key=os.getenv("OPENAI_API_KEY"),
            callback_manager=callback_manager
        )
        logger.debug("LLM initialized")
        
        # Initialize agent
        self.agent = self._create_agent()
        logger.info("CompanyResearchAgent initialized successfully")
        
    def get_company_logo(self, domain: str) -> str:
        """Get company logo from logo.dev"""
        try:
            logger.debug(f"Fetching logo for domain: {domain}")
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
                logger.debug(f"HEAD request failed, trying GET request for {domain}")
                response = requests.get(logo_url, headers=headers)
            
            if response.status_code == 200:
                logger.info(f"Successfully found logo for {domain}")
                return f"![{domain} logo]({logo_url})"
            logger.warning(f"Logo not found for {domain}, status code: {response.status_code}")
            return f"Logo not found for {logo_url} response: {response.status_code}"
        except Exception as e:
            logger.error(f"Error fetching logo for {domain}: {str(e)}")
            return f"Error fetching logo: {str(e)}"

    def get_company_news(self, company: str) -> List[Dict]:
        """Get recent news articles about the company using Tavily"""
        try:
            logger.info(f"Fetching news for company: {company}")
            search_result = self.tavily_client.search(
                query=f"Latest news and articles about {company}",
                search_depth="advanced",
                max_results=5,
                search_type="news",
                exclude_domains=["youtube.com", "facebook.com", "twitter.com", "instagram.com"],
                sort_by="relevance"
            )
            results = search_result.get('results', [])
            logger.info(f"Found {len(results)} news articles for {company}")
            return results
        except Exception as e:
            logger.error(f"Error fetching news for {company}: {str(e)}")
            return [{"error": f"Error fetching news: {str(e)}"}]
    
    def _create_agent(self) -> AgentExecutor:
        """Create and return the agent executor"""
        logger.debug("Creating agent executor")
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
        
        executor = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=self.tools,
            verbose=True
        )
        logger.debug("Agent executor created successfully")
        return executor
    
    def research_company(self, company: str) -> Dict:
        """Research a company and return the results"""
        try:
            logger.info(f"Starting company research for: {company}")
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
                logger.error(f"Error in agent response: {result['error']}")
                return {"Something went wrong parsing the response": result["error"]}
                
            # Extract information from the agent's response
            logger.info(f"Successfully completed research for {company}")
            return {
                "company": company,
                "agent_response": result["output"]
            }
        except Exception as e:
            logger.error(f"Error during company research: {str(e)}", exc_info=True)
            return {"Something went wrong": str(e)} 