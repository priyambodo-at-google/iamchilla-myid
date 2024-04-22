export GCP_REGION='asia-southeast2'
export GCP_PROJECT='iam-chilla'
export GCP_BUCKET='chillamyid-gemini-data'
export AR_REPO='chilla-myid-artifactregistry'  
export SERVICE_NAME='chilla-myid'

#pip install --upgrade pip
#pip install google-cloud-sdk
#gcloud init
#gcloud auth login
#gcloud config set project iam-chilla
#gcloud components update
#gcloud config set compute/region $GCP_REGION
#gcloud auth configure-docker "$GCP_REGION-docker.pkg.dev"
#gsutil mb -l $GCP_REGION -c STANDARD gs://$GCP_BUCKET