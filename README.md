# newsletter-agent

An AI agent htat monitors arXiv, PubMed, and Semantic Scholar for new publications, filters them for relevance to a researcher's interests, and delivers a summary digest by email on a scheduled cadence.

## Status

Early development. No working code yet.

## Planned Architecture

- **Retrieval** - scheduled queries to arXiv, PubMed, and Semantic Scholar APIs
- **Filtering** - LLM-based relevance scoring against researcher interest profile
- **Summarization** - short digest summaries generated per paper
- **Delivery** - email dispatch on a daily or weekly schedule

## Configuration

Researcher preferences (topics, labs, cadence) will be defined in a config file, making the agent reusable across different users without code changes.
