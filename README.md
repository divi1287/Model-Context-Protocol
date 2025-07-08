# Model-Context-Protocol

There is MCP client and MCP server

## MCP Server (Backend)
This is a Python backend (usually FastAPI or Flask) that:

* Defines tools (functions like search, summarize, classify, etc.).

* Hosts resources like prompt templates or model files.

* Provides an API like:
      bash,
      Copy,
      Edit,
      POST /query,
      GET /tools,
      GET /agent_config
  
* Key Components

   tools/: Python functions wrapped to be exposed as API tools.

   prompts/: Templates stored as YAML or JSON.

   server.py: Main MCP server to route the request through LangChain/LLM agent.


## MCP Client (React)
Create a reusable React frontend (MCP Client) that can load agents dynamically from the backend.

**Features**

   * Agent Selector Dropdown

   * Input box for query

   * Response window

   * Dynamically call /query endpoint

### To run the code 

 **Install Dependencies**

`pip install fastapi uvicorn transformers torch`

 **Start the MCP Server**

`uvicorn server:app --reload --port 8000`

 **Run the client**
 
  `python3 cli.py`

