from crewai import Agent
from llm.llm import llm

report_agent = Agent(
    name="Report Generator Agent",
    role="Generates a patient-friendly medical summary report",
    goal="Summarize user symptoms, questions, and diagnosis in a clear report for doctors",
    backstory="An expert report generator trained to compile clinical data into readable summaries for telemedicine.",
    llm=llm,
    verbose=True
)
