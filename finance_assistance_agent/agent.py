from google.adk.agents import LlmAgent
from google.adk.tools import google_search

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A Simple finance assistance that helps with user's finance goals.",
    instruction="""
        You are a friendly finance assistant.
        You can help answer user's feneric questions on finance and help plan
        their finance goals. Be more friendly and positive.
    """,
    tools=[google_search]
)

root_agent = finance_assistance_agent