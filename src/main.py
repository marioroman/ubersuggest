#!/usr/bin/env python3
import argparse
import os
import logging
from dotenv import load_dotenv
from company_agent import CompanyResearchAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('ubersuggest.log')
    ]
)
logger = logging.getLogger(__name__)

def main():
    # Load environment variables
    load_dotenv()
    logger.info("Environment variables loaded")
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Company Research Tool')
    parser.add_argument('--company', help='Company name or domain (e.g., stripe.com)', default='globant')
    args = parser.parse_args()
    
    # Get company name if not provided
    company = args.company
    if not company:
        company = input("Enter company name or domain (e.g., stripe.com): ")
    
    logger.info(f"Starting research for company: {company}")
    
    try:
        # Initialize the company research agent
        agent = CompanyResearchAgent()
        logger.debug("CompanyResearchAgent initialized")
        
        # Research the company
        logger.info(f"Beginning company research for {company}")
        results = agent.research_company(company)
        
        # Display results
        logger.info("Research completed successfully")
        print(f"Company: {results['company']}")
        print(results['agent_response'])
                    
    except Exception as e:
        logger.error(f"Error occurred during company research: {str(e)}", exc_info=True)
        print(f"Error: {str(e)}")
        return 1
    
    logger.info("Company research process completed")
    return 0

if __name__ == "__main__":
    exit(main()) 