from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from catalog_agent.agent import catalog_agent

# To load the user info in user's context (state)
def save_user_info(tool_context: ToolContext,
                   name: str,
                   email:str,
                   mobile:str):
    tool_context.state["name"] = name
    tool_context.state["email"] = email
    tool_context.state["mobile"] = mobile


root_agent = LlmAgent(
    name="ecommerce_agent",
    description="An ecommerce agent that manages the ecommerce workflow",
    model="gemini-2.0-flash",
    instruction="""
    Role: You are an ecommerce agent who can help the user with the product catalog, checkout, and order tracking.
    Workflow:
        - Greet the user and give a brief introduction about yourself on how can you help and then gathering user Details as mentioned
        below. Do not directly start gaterhing user information.
        - If you do not know, ask the user's name, email, and mobile number. Ask for only one piece of information at a time.
        - Once you have the above information, call the save_user_info() tool to save this information.
        - Then understand the user's intent. Are they looking for a new purchase or to track an existing order?
        - Based on the user's request, route it to one of your sub-agents:
            - catalog_agent - For new purchases, questions about products, prices, availability, etc.
            - checkout_agent - For checkout of items in the cart.
            - tracking_agent - For tracking an existing order.

    Rules:
    1. NEVER answer the question yourself. Always delegate to exactly one sub-agent.
    2. If the user's message clearly matches one category, immediately call that agent.
    3. If you are unsure, ask a short clarifying question instead of guessing.
    4. After a sub-agent responds, you may send that response back to the user as-is, without adding extra content.

    """,
    tools=[save_user_info],
    sub_agents=[catalog_agent]
)