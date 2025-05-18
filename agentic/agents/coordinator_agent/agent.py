from google.adk.agents import Agent
from contextlib import AsyncExitStack
from code_docs_agent.agent import create_agent as create_code_docs_agent
from file_system_agent.agent import create_agent as create_file_system_agent
from git_agent.agent import create_agent as create_git_agent

async def create_agent():
  """
  Create an agent that helps user writing code, accessing code docs, read and write files.
  """

  exit_stack = AsyncExitStack()
  await exit_stack.__aenter__()

  file_system_agent, file_system_agent_exit_stack = await create_file_system_agent()
  await exit_stack.enter_async_context(file_system_agent_exit_stack)

  code_docs_agent, code_docs_agent_exit_stack = await create_code_docs_agent()
  await exit_stack.enter_async_context(code_docs_agent_exit_stack)

  git_agent, git_agent_exit_stack = await create_git_agent()
  await exit_stack.enter_async_context(git_agent_exit_stack)

  agent = Agent(
    model='gemini-2.0-flash',
    name='coordinator_agent',
    description='Agent that can access sub agents to help user writing code, accessing code docs, read and write files.',
    instruction=
      'Your role is help user writing code, for that you need to manage and delagate instructions to sub agents'
      '',
    sub_agents=[
      file_system_agent,
      code_docs_agent,
      git_agent,
    ],
    )
  return agent, exit_stack


root_agent = create_agent()