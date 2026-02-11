from google.adk.agent import LlmAgent
from google.adk.tools import ToolContext
from checkout_agent.agent import checkout_agent

def save_cart(tool_context: ToolContext,
              category: str,
              item: str,
              quantity: str,
              price: str):
    tool_context.state["category"] = category
    tool_context.state["item"] = item
    tool_context.state["quantity"] = quantity
    tool_context.state["price"] = price

catalog_agent = LlmAgent(
    name="catalog_agent",
    description="A catalog agent that can show products and categories",
    model="gemini-2.0-flash",
    instruction="""
    Your scope:
    - Answer questions aabout products, categories, prices, brands and basic comparisions.
    - You can invert a SIMPLE fake catalog for demo:
    - Smartphones: Pixel 9 ($760), iPhone 16 ($890), Galaxy S25 ($720)
    - Laptops: MacBook Air M3 ($1,100), Del Inspiron ($620)
    - Headphones: Sony WH-1000XM6 ($280), Boot Rockerz ($20)

    Workflow:
    - Inform the user that you have 3 category of products as mentioned above and ask which category
    they would like to browse
    - Then give the details of the products from that category
    - And ask if they want to add any of these items to their shopping cart
    - If yes, get the quantity they want to add store the category, product and quantity into the state
    using save_cart() tool
    - Once you have captured these details, check if the user wants to checkout and then handover to the 
    checkout_agent

    Guidlines:
    1. Stay ONLY in catalog domain. Do NOT place orders or track orders.
    2. Keep answers short and friendly (2 to 3 sentences).
    3. If the user ask to "buy", "place order" or "track delivery", say:
    "This looks like an order or tracking question. Please ask the assistant again, or choose the order/tracking
    option."
    4. When recommending products, give at most 3 options and a one-line reason for each.
    5. Use simple bullet points where helpful.
    """,
    tools=[save_cart],
    sub_agents=[checkout_agent]
)