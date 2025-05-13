from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

async def create_agent():
  """
  Create an agent that helps user writting code, accessing code docs, read and writte files.
  """

  agent = LlmAgent(
      model='gemini-2.0-flash',
      name='code_docs_agent',
      description='Agent that can access sub agents to help user writting code, accessing code docs, read and writte files.',
      instruction=
        'Your role is help user writting code!'
        ' you need to access sub agents to do that.',
  )
  return agent, exit_stack


root_agent = create_agent()