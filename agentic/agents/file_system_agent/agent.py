from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

async def create_agent():
  """
  Create an agent that can access and operates file system.
  """
  tools, exit_stack = await MCPToolset.from_server(
      connection_params=StdioServerParameters(
          command='npx',
          args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/mnt/c/dev/",
          ],
      )
  )

  agent = LlmAgent(
      model='gemini-2.0-flash',
      name='file_system_agent',
      description=
      'Agent that can access the file system'
      ' and help the user with file system operations.'
      ' The agent can read and write files,',
      instruction=
        'Help user accessing their file systems'
        ' and help them with file system operations.'
        ' The agent can read and write files,',
      tools=tools,
  )
  return agent, exit_stack


root_agent = create_agent()