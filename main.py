from dotenv import load_dotenv
from crewai import Task, Crew
from llm.llm import llm
from agents.symptom_agent import symptom_agent
from agents.followup_agent import followup_agent
from agents.diagnosis_agent import diagnosis_agent
from agents.report_agent import report_agent

load_dotenv()

symptom_task   = Task(agent=symptom_agent,   description="Extract and format symptoms from user input", expected_output="Structured JSON…")
followup_task  = Task(agent=followup_agent,  description="Ask follow-up questions based on symptoms",       expected_output="Relevant follow-up questions")
diagnosis_task = Task(agent=diagnosis_agent, description="Suggest possible medical conditions",            expected_output="List of potential diagnoses with probability scores")
report_task    = Task(agent=report_agent,    description="Generate a summary report for doctors",         expected_output="Formatted medical report summarizing all information")

crew = Crew(
    agents=[symptom_agent, followup_agent, diagnosis_agent, report_agent],
    tasks=[symptom_task, followup_task, diagnosis_task, report_task],
    default_llm=llm,
    verbose=True
)

if __name__ == "__main__":
    print(crew.kickoff())
