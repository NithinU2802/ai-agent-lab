from google.adk.agents import LlmAgent
from google.adk.tools import google_search

investment_plan_agent = LlmAgent(
    name="investment_plan_agent",
    model="gemini-2.5-flash",
    description="An investment plan assistant who can use Google Search to find latest information" \
    "and assist users in creating a savings plan",
    instructions="""
        You are a friendly finance assistance.
        you can help analyse user's monthly spending and find out ways to
        reduce spending and increase savings to achieve their goal.

        ALWAYS use the google_search tool when asked about:
        - Stock price (e.g., "Tesla stock price", "TSLA latest price")
        - Market data, financial news, or company information
        - ANY question containing words like "latest", "current", "today", "now", "recent"

        After searching, provide the factual data from the search results with specific number.
    """,
    tools=[google_search]
)