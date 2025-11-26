"""
Context7 MCP Integration for Real Web Search

This module provides real web search capabilities using Context7's MCP server.
"""

import os
import asyncio
import httpx
from typing import List, Optional


class Context7Search:
    """Context7 web search client using MCP protocol."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Context7 search client.
        
        Args:
            api_key: Context7 API key (defaults to CONTEXT7_API_KEY env var)
        """
        self.api_key = api_key or os.getenv("CONTEXT7_API_KEY")
        self.base_url = "https://api.context7.com/v1"
        
    async def search(self, query: str, max_results: int = 5) -> List[dict]:
        """
        Perform web search using Context7.
        
        Args:
            query: Search query
            max_results: Maximum number of results to return
            
        Returns:
            List of search result dictionaries
        """
        if not self.api_key or self.api_key.startswith("dummy"):
            # If no real API key, return empty to trigger fallback
            return []
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/search",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "query": query,
                        "max_results": max_results
                    },
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return data.get("results", [])
                else:
                    print(f"Context7 search failed with status {response.status_code}")
                    return []
                    
        except Exception as e:
            print(f"Context7 search error: {e}")
            return []
    
    async def fetch_content(self, url: str) -> str:
        """
        Fetch webpage content using Context7.
        
        Args:
            url: URL to fetch
            
        Returns:
            Webpage content as text
        """
        if not self.api_key or self.api_key.startswith("dummy"):
            return f"Content from {url} (Context7 API key required for real data)"
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/fetch",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={"url": url},
                    timeout=30.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    return data.get("content", "")
                else:
                    return f"Failed to fetch {url}"
                    
        except Exception as e:
            return f"Error fetching {url}: {e}"


# Fallback: Simple web scraping without Context7
async def fallback_search(query: str, max_results: int = 5) -> List[dict]:
    """
    Fallback search using direct web scraping.
    
    Args:
        query: Search query
        max_results: Maximum results
        
    Returns:
        List of search results
    """
    try:
        # Use DuckDuckGo HTML search as fallback
        from bs4 import BeautifulSoup
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://html.duckduckgo.com/html/",
                params={"q": query},
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10.0
            )
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            for result in soup.find_all('div', class_='result')[:max_results]:
                title_elem = result.find('a', class_='result__a')
                snippet_elem = result.find('a', class_='result__snippet')
                
                if title_elem:
                    results.append({
                        'title': title_elem.get_text(strip=True),
                        'url': title_elem.get('href', ''),
                        'snippet': snippet_elem.get_text(strip=True) if snippet_elem else ''
                    })
            
            return results
            
    except Exception as e:
        print(f"Fallback search error: {e}")
        return []


async def fallback_fetch(url: str) -> str:
    """
    Fallback webpage fetching.
    
    Args:
        url: URL to fetch
        
    Returns:
        Page content
    """
    try:
        from bs4 import BeautifulSoup
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10.0,
                follow_redirects=True
            )
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            # Limit length
            if len(text) > 5000:
                text = text[:5000] + "..."
            
            return text
            
    except Exception as e:
        return f"Error fetching {url}: {e}"
