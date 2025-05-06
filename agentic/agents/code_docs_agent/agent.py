from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

async def create_agent():
  """
  Create an agent that can access code docs with context7.
  """
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='npx',
          args=[
            "-y",
            "@upstash/context7-mcp@latest",
          ],
      )
  )

  agent = LlmAgent(
      model='gemini-2.0-flash',
      name='code_docs_agent',
      description=
      'Agent that can access code docs with context7.'
      ' and help the user with code documentation.'
      ' e.g. javascript, python, many packages, like react, etc.',
      instruction=
        'Help user accessing code docs'
        ' e.g. languages like, javascript, python, packages, modules, like react, frameworks, like nestjs etc.',
      tools=tools,
  )
  return agent, exit_stack


root_agent = create_agent()