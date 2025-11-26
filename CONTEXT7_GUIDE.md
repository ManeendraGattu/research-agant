# Context7 Integration Guide

## What is Context7?

Context7 provides real-time web search capabilities through the Model Context Protocol (MCP). It allows your research agent to fetch actual, current data from the web instead of using mock data.

## Setup

### 1. Get Context7 API Key (Optional but Recommended)

Visit [Context7](https://context7.com/) to sign up and get your API key.

### 2. Add to Environment

Edit your `.env` file:

```bash
CONTEXT7_API_KEY=your-actual-context7-api-key
```

### 3. That's It!

The research agent will automatically use Context7 when available. If no API key is provided, it falls back to free web scraping.

## How It Works

The agent now uses **real web search** in two ways:

1. **Context7 (Primary)** - If you provide an API key:
   - High-quality web search results
   - Content extraction from web pages
   - Fast and reliable

2. **Fallback (Free)** - If no Context7 key:
   - Uses DuckDuckGo HTML search
   - Direct web scraping with BeautifulSoup
   - No API key required, but slower

## Benefits

✅ **Real Data** - Get actual current information from the web
✅ **Better Answers** - AI has access to real sources
✅ **Current Info** - Access to latest news and developments
✅ **Source Citations** - Real URLs and sources
✅ **Fallback Support** - Works even without API key

## Testing

Run your agent as usual:

```bash
python main.py
```

Try queries like:
- "Latest news in AI"
- "Current trends in technology"
- "Recent developments in quantum computing"

The agent will now fetch REAL data from the web!

## Troubleshooting

**Q: I don't have a Context7 API key**
- A: No problem! The agent will use the free fallback search automatically.

**Q: Search is slow**
- A: Free fallback is slower than Context7. Consider getting an API key for better performance.

**Q: Not getting results**
- A: Check your internet connection. The fallback requires web access.

## Cost

- **Context7**: Check their pricing at context7.com
- **Fallback**: Completely free, no API key needed

---

Now your research agent gets REAL web data! 🌐
