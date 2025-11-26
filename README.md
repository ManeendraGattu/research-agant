# Research Agent with Pydantic AI and Logfire

A powerful research agent built with **Pydantic AI** and monitored with **Logfire** for comprehensive observability. This agent can search the web, fetch content, analyze information, and synthesize research findings.

- **Intelligent Research**: Conducts comprehensive research using LLM-powered analysis
- **Multiple Tools**: Web search, content fetching, and content analysis capabilities
- **Logfire Integration**: Full observability with detailed traces, logs, and metrics
- **Type-Safe**: Built with Pydantic for robust data validation
- **Async Operations**: Efficient asynchronous execution
- **Structured Output**: Returns well-formatted, structured research findings
- **Extensible**: Easy to add new tools and capabilities

## Prerequisites

- Python 3.10 or higher
- OpenAI API key (or other LLM provider)
- Logfire account and token (optional but recommended)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd research_agent
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your actual tokens:
   ```env
   OPENAI_API_KEY=your-actual-openai-api-key
   LOGFIRE_TOKEN=your-actual-logfire-token
   LOGFIRE_PROJECT_NAME=research-agent
   ```

## 🔑 Getting Your Tokens

### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy and paste it into your `.env` file

### Logfire Token
1. Go to [Logfire](https://logfire.pydantic.dev/)
2. Sign up for an account
3. Create a new project
4. Copy your project token
5. Paste it into your `.env` file

> **Note**: The application will work without Logfire (with warnings), but you won't get observability features.

## 💻 Usage

### Interactive Mode (Default)

Simply run the main script to start researching:

```bash
python main.py
```

This starts an interactive session where you can:
- Enter your research topics when prompted
- Get comprehensive research results with summaries, key findings, and sources
- Research multiple topics in one session
- Type 'quit' to exit

Example session:
```
💬 Enter your research topic: What are the latest trends in AI agents?
🔍 Researching...

RESEARCH RESULTS
================
📊 Summary: [AI-generated comprehensive summary]
🔑 Key Findings:
  1. [Finding 1]
  2. [Finding 2]
  ...
📚 Sources: [List of sources]

Would you like to research another topic? (y/n): y

� Enter your research topic: Tell me about Pydantic AI
...
```

### Alternative: Advanced Chatbot with History

For a feature-rich chatbot with conversation history:

```bash
python chatbot.py
```

Features:
- Conversation history tracking
- Configuration viewing
- History management commands
- Enhanced user interface

### Alternative: Quick Chat (Minimal)

For a simpler interface:

```bash
python quick_chat.py
```

### Using the Agent in Your Code

```python
import asyncio
from research_agent import ResearchAgent

async def main():
    # Initialize the agent
    agent = ResearchAgent()
    
    # Perform research
    results = await agent.research(
        "What are the latest developments in AI agents?",
        max_results=5
    )
    
    # Access structured results
    print(f"Summary: {results.summary}")
    print(f"Key Findings: {results.key_findings}")
    print(f"Sources: {results.sources}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Quick Search

For a simple text summary:

```python
async def quick_example():
    agent = ResearchAgent()
    summary = await agent.quick_search("Benefits of Pydantic AI")
    print(summary)

asyncio.run(quick_example())
```

## 🛠️ Architecture

### Components

1. **ResearchAgent**: Main agent class that orchestrates research operations
2. **Tools**: Registered functions that the agent can call:
   - `search_web`: Searches for information (mock implementation)
   - `fetch_webpage_content`: Fetches and extracts webpage content
   - `analyze_content`: Analyzes content with specific focus

3. **Data Models**:
   - `ResearchDependencies`: Dependencies injected into tool context
   - `SearchResult`: Structure for search results
   - `ResearchFindings`: Structured output from research

### Logfire Integration

Logfire provides complete observability:
- **Traces**: Full execution traces of agent operations
- **Logs**: Detailed logging of all tool calls
- **Metrics**: Performance and success metrics
- **Error Tracking**: Automatic error capture and reporting

Access your Logfire dashboard to view:
- Agent execution flow
- Tool call sequences
- Performance bottlenecks
- Error diagnostics

## 🔧 Customization

### Adding New Tools

Register custom tools by adding methods with the `@agent.tool` decorator:

```python
@self.agent.tool
async def custom_tool(
    ctx: RunContext[ResearchDependencies],
    param: str
) -> str:
    """Your custom tool description."""
    if self.logfire_enabled:
        logfire.info("Custom tool called", param=param)
    
    # Your implementation
    return result
```

### Using Different LLM Providers

Change the model when initializing:

```python
# Use GPT-4
agent = ResearchAgent(model_name="openai:gpt-4")

# Use Claude
agent = ResearchAgent(model_name="anthropic:claude-3-opus")

# Use Gemini
agent = ResearchAgent(model_name="google:gemini-pro")
```

### Integrating Real Search APIs

Replace the mock search implementation with real APIs:

```python
# Install search API library
pip install google-search-results  # for SerpAPI

# Update the search_web tool
async def search_web(ctx, query):
    from serpapi import GoogleSearch
    search = GoogleSearch({
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY")
    })
    return search.get_dict()["organic_results"]
```

## 📊 Output Format

The agent returns structured `ResearchFindings`:

```python
{
    "query": "Your research query",
    "summary": "Comprehensive summary of findings",
    "key_findings": [
        "Finding 1",
        "Finding 2",
        "Finding 3"
    ],
    "sources": [
        "https://source1.com",
        "https://source2.com"
    ],
    "timestamp": "2024-11-24T10:30:00"
}
```

## 🧪 Testing

Run the included demos to test functionality:

```bash
# Run all demos
python main.py

# Run specific demo (modify main.py to comment out others)
python main.py
```

## 📝 Examples

### Example 1: Technology Research

```python
agent = ResearchAgent()
results = await agent.research(
    "Compare React vs Vue.js for frontend development"
)
```

### Example 2: Market Research

```python
agent = ResearchAgent()
results = await agent.research(
    "Current trends in electric vehicle market 2024",
    max_results=10
)
```

### Example 3: Academic Research

```python
agent = ResearchAgent()
results = await agent.research(
    "Recent advances in quantum computing algorithms"
)
```

## 🐛 Troubleshooting

### Issue: "OpenAI API key not found"
- **Solution**: Make sure you've created a `.env` file and added your API key

### Issue: "Logfire connection failed"
- **Solution**: This is just a warning. The agent will work without Logfire, but you won't get observability features. Add a valid token to enable it.

### Issue: "Module not found"
- **Solution**: Make sure you've activated your virtual environment and installed all dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure
- Use environment variables for all sensitive data
- The `.gitignore` file is configured to exclude `.env`

## 📚 Resources

- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [Logfire Documentation](https://logfire.pydantic.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

Feel free to extend this agent with:
- Additional tools (PDF parsing, image analysis, etc.)
- More LLM providers
- Enhanced error handling
- Custom result formatters
- Integration with vector databases

## 📄 License

This project is provided as-is for educational and development purposes.

## 🎯 Next Steps

1. Replace dummy tokens with real API keys
2. Test the agent with various queries
3. Explore the Logfire dashboard for insights
4. Customize tools for your specific use case
5. Integrate with real search APIs for production use

---

**Built with ❤️ using Pydantic AI and Logfire**
