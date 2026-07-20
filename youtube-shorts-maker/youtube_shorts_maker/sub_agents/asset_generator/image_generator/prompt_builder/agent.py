from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .model import PromptBuilderOutput
from .prompt import PROMPT_BUILDER_DESCRIPTION, PROMPT_BUILDER_PROMPT

MODEL = LiteLlm(model="openai/gpt-4o")

prompt_builder_agent = Agent(
    name="PromptBuilderAgent",
    description=PROMPT_BUILDER_DESCRIPTION,
    instruction=PROMPT_BUILDER_PROMPT,
    model=MODEL,
    output_schema=PromptBuilderOutput,
    output_key="prompt_builder_output",
)
