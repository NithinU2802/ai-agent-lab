from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
import json
from tools import search_tool
from tools import wiki_tool
from tools import save_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_user: list[str]


llm1 = ChatOpenAI(
    model="gpt-4o-mini"
)

# llm2 = ChatAnthropic(
#     model="claude-3-5-sonnet-20241022"
# )

parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a research assistant that will help generate a research paper.
    Answer the user query and use necessary tools.
    Wrap the output in this format and provide no other text:
    {format_instructions}
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm=llm1,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
input = input("How can I help you rearch today? ")
raw_response = agent_executor.invoke(
    {"input": input}
)

# print(raw_response)

# llm2
# json_response = json.loads(raw_response.get("output"))
# structured_response = parser.parse(json_response["summary"])

# Convert JSON string into dict
json_response = json.loads(raw_response["output"])

# Parse the full dict to verify structure
structured_response = parser.parse(json.dumps(json_response))  # Adjust based on actual structure
# print(structured_response)

# To get summary of json outcome
# print("Here is the summary: ", json_response['summary'])

try:
    # print("Here is the topic: ", structured_response.topic)
    print(structured_response)
    # Save the structured response to a file
    save_tool.run(json.dumps(json_response, indent=2))
except Exception as e:
    print("Error parsing response", e, "Raw response:", raw_response)
