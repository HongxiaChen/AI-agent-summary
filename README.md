# AI-Agent-Summary

AI-Agent-Summary is a Python-based AI project that creates virtual agents to extract and summarize information from websites. 
It uses OpenAI's API and CrewAI framework to generate intelligent responses.

# Installation
## Clone the Repository
```
sh
git clone git@github.com:yourusername/AI-agent-summary.git
cd AI-agent-summary
```
## Create a Virtual Environment
```
conda env create -f environment.yml
conda activate ai_agent_env
```
## Create a `.evn`file and add the following inside .env (Replace Openai_api_key with your actual key)
```
OPENAI_API_KEY = openai_api_key
OPENAI_MODEL_NAME = gpt-4
```
## Run Python Script
To run the AI agent script, execute:
```
python AI_agent_crewai_test.py
```
## Expected Output
```
Agent Nr1
<Summary of * >
Agent Nr2
<Summary of the given website>
```
## Project Structure
```
│── .gitignore              # Ignored files like .env and venv
│── README.md               # Documentation (this file)
│── requirements.txt        # Python package dependencies
│── environment.yml         # Conda environment file
│── AI_agent_crewai_test.py # AI agent script
└── .env                    # API keys (not committed)
```
# Contact
For questions or suggestions, contact me:
📧 Email: hongxia.chen06@gmail.com  
🔗 GitHub: [Hongxia Chen](https://github.com/HongxiaChen)
