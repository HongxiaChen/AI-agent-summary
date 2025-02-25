#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:44:52 2025

@author: hongxia.chen
"""

import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_model_name = os.getenv("OPENAI_MODEL_NAME")

# Define URL variable
web_url = "https://medium.com/@elisowski/a-list-of-ai-agents-set-to-dominate-in-2025-028f975c5b99"
# "https://www.adressa.no/sport/ski-vm/i/731ebv/uttak-disse-skal-gaa-vms-tre-foerste-oevelser"

# Define Agents
info_agent = Agent(
    role = "Information Agent",
    goal = "give compleling information about a certain topic",
    backstory = """
    You love to know information. People love and hate you for it. You win most of quizzes at your local pub.
    """
    )

summary_agent = Agent(
    role = "Summary Content",
    goal = "Summary content based on an given website",
    backstory = """
    You are a good summarizer and translator
    """
    )
# Define Tasks
task1 = Task(
    description = "Tell me all about Adresseavisen",
    expected_output = "Give me a quick summary and then also give me 7 bullet point",
    agent = info_agent
    )

task2 = Task(
    description = "Summarize on given website, {web_url}",
    expected_output = "Give me a quick summary",
    agent = summary_agent
    )

# Define Crews
crew = Crew(
    agents=[info_agent],
    tasks = [task1],
    verbose = False
    )

crew_2 = Crew(
    agents = [summary_agent],
    tasks = [task2],
    verbose = False
    )

# Run the tasks
result = crew.kickoff()
result_2 = crew_2.kickoff()

# Print results
print("***********************")
print("###### AGENT Nr1")
print("***********************")
print(result)

print("***********************")
print("###### AGENT Nr2")
print("***********************")
print(result_2)