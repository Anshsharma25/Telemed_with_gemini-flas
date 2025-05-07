# agents/symptom_agent.py
from crewai import Agent

symptom_agent = Agent(
    name="Symptom Intake Agent",
    role="Parses symptoms",
    goal="Convert user input to structured symptom data",
    backstory="Expert in understanding layman medical descriptions",
    verbose=True       # ← no per‑agent llm param
)
