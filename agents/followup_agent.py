from crewai import Agent
from llm.llm import llm

followup_agent = Agent(
    name="Follow-up Question Agent",
    role="Asks clarifying questions based on symptoms",
    goal="Determine any missing medical information from the user",
    backstory="An expert in clinical questioning to get the full picture.",
    llm=llm,
    verbose=True
)
