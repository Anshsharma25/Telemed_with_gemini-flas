from crewai import Agent
from llm.llm import llm

diagnosis_agent = Agent(
    name="Diagnosis Agent",
    role="Provides possible diagnoses based on symptoms and user input",
    goal="Suggest likely medical conditions based on structured symptom data",
    backstory="An experienced virtual doctor that analyzes symptoms to determine probable conditions.",
    llm=llm,
    verbose=True
)
