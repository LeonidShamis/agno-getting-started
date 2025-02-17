# https://docs.agno.com/examples/getting-started/basic-agent

"""
This example shows how to create a basic AI agent with a distinct personality. We’ll create a fun news reporter that combines NYC attitude with creative storytelling. This shows how personality and style instructions can shape an agent’s responses.

Example prompts to try:

“What’s the latest scoop from Central Park?”
“Tell me about a breaking story from Wall Street”
“What’s happening at the Yankees game right now?”
“Give me the buzz about a new Broadway show”
"""

# Use Ollama with a local LLM instead of OpenAI

from textwrap import dedent

from agno.agent import Agent
# from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama
from ollama import Client as OllamaClient
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3.2:3b-instruct-q8_0")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

# Create our News Reporter with a fun personality
agent = Agent(
    # model=OpenAIChat(id="gpt-4o"),
    model=Ollama(id=OLLAMA_MODEL_NAME, client=OllamaClient(host=OLLAMA_HOST)),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Your style guide:
        - Start with an attention-grabbing headline using emoji
        - Share news with enthusiasm and NYC attitude
        - Keep your responses concise but entertaining
        - Throw in local references and NYC slang when appropriate
        - End with a catchy sign-off like 'Back to you in the studio!' or 'Reporting live from the Big Apple!'

        Remember to verify all facts while keeping that NYC energy high!\
    """),
    markdown=True,
)

# Example usage
agent.print_response(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)

# More example prompts to try:
"""
Try these fun scenarios:
1. "What's the latest food trend taking over Brooklyn?"
2. "Tell me about a peculiar incident on the subway today"
3. "What's the scoop on the newest rooftop garden in Manhattan?"
4. "Report on an unusual traffic jam caused by escaped zoo animals"
5. "Cover a flash mob wedding proposal at Grand Central"
"""