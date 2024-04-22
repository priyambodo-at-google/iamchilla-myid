export GCP_REGION='asia-southeast2'
export GCP_PROJECT='iam-chilla'
export GCP_BUCKET='chillamyid-gemini-data'
export AR_REPO='chilla-myid-artifactregistry'  
export SERVICE_NAME='chilla-myid'                 

pip install --upgrade pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip