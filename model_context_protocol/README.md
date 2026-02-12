# MCP - Model Context Protocol  

## Detaching and Decoupling Tools from the Agent

---

## AI Agents Without MCP

Consider an agent working with:

- LLM (GPT Model)  
- Google Maps Route API  
- Booking.com API  

### Architecture Example 1

```bash
user <--> AI AGENT <--> Google Maps Route API and Booking.com API
            ^
            |
            v
        LLM (GPT Model)
```

### Architecture Example 2 (More Tools Added)

```bash
user <--> AI AGENT <--> Google Maps Route API, Google Maps Places API, and Booking.com API
            ^
            |
            v
        LLM (GPT Model)
```

---

## Problems Without MCP

- **Agent knows too many low-level details**
  - Request/Response schema management  
  - Data parsing  
  - Error handling  
  - Retry mechanisms  

- **Tight coupling of tools with agents**
  - Agent must be instructed on how to use each tool  
  - Tools cannot be easily reused in another application  

- **Agent complexity increases** as more tools are added  

> **Note:** Anthropic developed MCP after facing these challenges while building multiple agents for their use cases.

---

# MCP (Model Context Protocol)

### Example MCP Server

- **Google Maps MCP Server**
  - `Search_Tool`
  - `Routes_Tool`
  - `Places_Tool`

---

## MCP Architecture

- MCP follows a **Client-Server architecture**
- The **Agent acts as the client**
- MCP Server exposes tools

### Flow

1. Agent requests the list of available tools from the MCP server.
2. MCP server provides tool metadata.
3. Agent sends available tool information along with the user prompt to the LLM.
4. LLM selects the required tool and formats the input properly.
5. MCP server executes the tool with the given input.
6. MCP returns the tool output to the Agent.
7. Agent sends tool output along with the user prompt back to the LLM.
8. LLM generates a natural language response.
9. Final response is displayed to the user via chatbot.

---

## Why MCP?

### Reusability
- Tools can be used across multiple agents.

### Loose Coupling
- Agents are not tightly bound to specific tool implementations.
- Easy to replace or modify MCP servers in the future.

### Scalability
- Add or modify tools without significantly changing agent logic.
- Improves agent capability while maintaining simplicity.

---

# General Question

> It seems like a library of tools so why is it called a *protocol*?

---

## Why MCP is a Protocol

MCP is called a **protocol** because:

- **Standardized Message Exchange**
  - Defines structured communication format between agent and server.

- **Interoperability Through Standardization**
  - Any MCP-compatible client can communicate with any MCP-compatible server.

-  **Uses JSON-RPC for Communication**
  - Structured request/response format.

---

## Analogy

Just like:

- **HTTP** is a protocol with defined rules for communication over the web,  

**MCP** defines standardized rules and message formats for communication between agents and tool servers.
 