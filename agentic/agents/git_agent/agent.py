import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

async def create_agent():
  """
  Create an agent that can access and operates git commands.
  """
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='mcp-server-git',
      )
  )

  model = LiteLlm(
    model='gemini/gemini-2.0-flash',
    api_key=os.getenv('GOOGLE_API_KEY')
  )

  agent = Agent(
      model=model,
      name='git_agent',
      description=
      'Agent that can access the git commands'
      ' and help the user with git operations.',
      instruction=
        'Help user performing git commands'
        ' if the user ask for a feature, create a new branch feature/feature-name'
        ' if the user ask for a fix, create a new branch hotfix/fix-name'
        ' and help them with git operations.',
      tools=tools,
  )
  return agent, exit_stack


root_agent = create_agent()