#!/usr/bin/env python3
import argparse
import os
from dotenv import load_dotenv
from company_agent import CompanyResearchAgent

def main():
    # Load environment variables
    load_dotenv()
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Company Research Tool')
    parser.add_argument('--company', help='Company name or domain (e.g., stripe.com)', default='globant')
    args = parser.parse_args()
    
    # Get company name if not provided
    company = args.company
    if not company:
        company = input("Enter company name or domain (e.g., stripe.com): ")
    
    try:
        # Initialize the company research agent
        agent = CompanyResearchAgent()
        
        # Research the company
        print(f"\nResearching {company}...")
        results = agent.research_company(company)
        
        # Display results
        print(f"Company: {results['company']}")
        print(results['agent_response'])
                    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 