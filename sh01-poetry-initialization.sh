#/bin/bash
poetry shell #--> Just do this if you already install and configure your Poetry

#------------------------------------------------------------------------------
#Do this if you haven't install and configure your Poetry
brew install python
brew link python@3.11
brew install pip

sudo pip install --upgrade pip
sudo pip install --upgrade poetry
rm pyproject.toml
rm poetry.lock

#Initialize the Poetry environment 
poetry new chilla.v1.0 #(optional)
poetry init

#Activate the environment in your directory
poetry config virtualenvs.in-project true
poetry install
poetry shell

#Add your Python Dependency Package (based on your needs)
poetry add streamlit
poetry add google-cloud-aiplatform
poetry add google-cloud-logging
poetry add langchain
poetry add pytz
poetry add google-cloud-discoveryengine
poetry add transformers

#Create requirements.txt (optional)
poetry export -f requirements.txt --output requirements.txt

#Operational that you might need (optional)
poetry remove streamlit #removing package
poetry install --no-root #optional if you change toml manual
poetry lock #optional if you change toml manual
poetry env list
poetry env info
poetry show --tree
poetry show --latest
poetry exit
poetry update
deactivate #deactivate the environment