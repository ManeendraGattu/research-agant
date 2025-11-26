"""
Main entry point for the Research Agent - Interactive Mode

This script allows users to input their own research queries
and get real-time results from the research agent.
"""

import asyncio
import json
import sys
import time
from research_agent import ResearchAgent, ResearchFindings


async def interactive_research():
    """Interactive research mode - user inputs their own query."""
    print("\n" + "🔬" * 35)
    print("      RESEARCH AGENT - INTERACTIVE MODE")
    print("      Powered by Pydantic AI + Gemini")
    print("🔬" * 35 + "\n")
    
    # Initialize agent
    print("Initializing research agent...")
    agent = ResearchAgent()
    print("✅ Agent ready!\n")
    
    while True:
        print("="*70)
        print("What would you like to research?")
        print("(Type 'quit' to exit, 'help' for commands)")
        print("="*70)
        
        # Get user input
        await asyncio.sleep(3)
        query = input("\nEnter your research topic: ").strip()
        
        # Handle empty input
        if not query:
            continue
        
        # Handle commands
        if query.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using Research Agent!")
            print("Goodbye!\n")
            break
        
        # Perform research
        print(f"\n🔍 Researching: {query}")
        print("⏳ Please wait while I gather and analyze information...\n")
        
        try:
            results = await agent.research(query, max_results=5)
            
            # Display results
            print("="*70)
            print("RESEARCH RESULTS")
            print("="*70)
            print(f"\n Summary:")
            print(results.summary)
            
            print("\n Key Findings:")
            for i, finding in enumerate(results.key_findings, 1):
                print(f"  {i}. {finding}")
            
            print("\n Sources:")
            for i, source in enumerate(results.sources, 1):
                print(f"  {i}. {source}")
            
            print(f"\n Completed at: {results.timestamp}")
            print("="*70 + "\n")
            
            # Ask if user wants to continue
            continue_choice = input("Would you like to research another topic? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes', '']:
                print("\n👋 Thank you for using Research Agent!")
                print("Goodbye!\n")
                break
            
        except Exception as e:
            print(f"\n Error during research: {e}")
            print("Please try again with a different query.\n")
            
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            if retry not in ['y', 'yes', '']:
                print("\n Goodbye!\n")
                break





async def main():
    """Main entry point - run interactive research mode."""
    try:
        await interactive_research()
    except KeyboardInterrupt:
        print("\n\n Interrupted by user")
        print(" Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your configuration and try again.\n")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
