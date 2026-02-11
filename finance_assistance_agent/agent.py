from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from typing import Dict
from investment_plan_agent.agent import investment_plan_agent

def get_user_personal_finance_details() -> Dict:
    return {
        "salary": 50000,
        "expense": {
            "EMI_Expense": 25000,
            "Essentials": 5000,
            "Entertainment": 5000,
            "Shopping and Travel": 5000
        },
        "savings": 10000
    }

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistant that helps with user's finance goals.",
    instructions="""
        You are a friendly finance assistant.
        You can help answer user's generic questions on finance and help plan
        their finance goals. Be more friendly and positive.

        You have two tools to use to complete your task.
        1. get_user_personal_finance_details - This tool will give you the user's current financial details.
        2. investment_plan_agent - This tool can perform Google Search to get any latest information
        from websites and will be able to ask more details from the user and plan their savings goal.

        ALWAYS use the investment_plan_agent with google_search tool when asked about:
        - Stock price (e.g., "Tesla stock price", "TSLA latest price")
        - Market data, financial news, or company information
        - ANY question containing words like "latest", "current", "today", "now", "recent"
    """,
    tools=[
        AgentTool(investment_plan_agent), # we passing agent as a tool 
        AgentTool(get_user_personal_finance_details)
    ]
)


root_agent = finance_assistance_agent