from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import (
    AGENT_CARD_WELL_KNOWN_PATH,
    RemoteA2aAgent,
)
from google.adk.models.lite_llm import LiteLlm

load_dotenv()


history_agent = RemoteA2aAgent(
    name="HistoryHelperAgent",
    description="An agent that can help students with their history homework",
    agent_card=f"http://127.0.0.1:8001{AGENT_CARD_WELL_KNOWN_PATH}",
)

philosophy_agent = RemoteA2aAgent(
    name="PhilosophyHelperAgent",
    description="An agent that can help students with their philosophy homework",
    agent_card=f"http://127.0.0.1:8002{AGENT_CARD_WELL_KNOWN_PATH}",
)

root_agent = Agent(
    name="StudentHelperAgent",
    description="An agent that can helps students with their homework",
    model=LiteLlm(model="openai/gpt-4o-mini"),
    sub_agents=[
        history_agent,
        philosophy_agent,
    ],
)
