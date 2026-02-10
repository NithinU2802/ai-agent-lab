# AI Agent Learning and Implementation

This project demonstrates a basic implementation of an AI Agent, including setup and execution instructions.

## Getting Started

### 1. Create a Virtual Environment

Create a new Python virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

Install the required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

This project requires API keys for AI models. You can create either of below:

- **OpenAI:** [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) 

**(or)**

- **Anthropic:** [https://console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

After generating your keys, add them to your environment variables:
```bash
OPENAI_API_KEY="your_openai_key"
ANTHROPIC_API_KEY="your_anthropic_key"
```
`Note: If you use ANTHROPIC_API_KEY then modify the llm usage accordingly.`

### 4. Run the Project

Execute the main script:

```bash
python main.py
```


# Agent Development Kit

```bash
User Request
└── Base Agent
    ├── Task Analysis & Planning
    │
    ├── Tools
    │   ├── Custom Tools
    │   │   ├── Python Functions
    │   │   ├── External APIs
    │   │   └── Internal Services
    │   │
    │   └── Built-in Tools
    │       ├── Google Search
    │       ├── Vertex AI Search
    │       └── BigQuery Analytics
    │
    ├── Sub Agents
    │   ├── LLM Sub-Agent
    │   │   ├── Domain-Specific Reasoning
    │   │   ├── Independent Prompt & Context
    │   │   └── Structured / Text Output
    │   │
    │   └── Workflow Agent
    │       ├── Sequential Agent
    │       │   └── Step-by-Step Execution
    │       │
    │       ├── Parallel Agent
    │       │   └── Concurrent Task Execution
    │       │
    │       └── Loop Agent
    │           └── Iterative Execution Until Condition Met
    │
    └── Final Response
```