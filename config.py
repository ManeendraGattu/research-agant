"""
Configuration module for the Research Agent.

Handles loading environment variables and configuration settings.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration settings for the research agent."""
    
    # API Keys
    GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY")
    LOGFIRE_TOKEN: Optional[str] = os.getenv("LOGFIRE_TOKEN")
    
    # Logfire Settings
    LOGFIRE_PROJECT_NAME: str = os.getenv("LOGFIRE_PROJECT_NAME", "research-agent")
    LOGFIRE_ENABLED: bool = os.getenv("LOGFIRE_ENABLED", "true").lower() == "true"
    
    # Optional Search API Keys
    SERPER_API_KEY: Optional[str] = os.getenv("SERPER_API_KEY")
    TAVILY_API_KEY: Optional[str] = os.getenv("TAVILY_API_KEY")
    
    # Agent Settings
    DEFAULT_MODEL: str = os.getenv("DEFAULT_MODEL", "gemini-2.0-flash")
    MAX_SEARCH_RESULTS: int = int(os.getenv("MAX_SEARCH_RESULTS", "5"))
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
    
