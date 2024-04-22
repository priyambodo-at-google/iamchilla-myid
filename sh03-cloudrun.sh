#/bin/bash
export GCP_REGION='asia-southeast2'
export GCP_PROJECT='iam-chilla'
export GCP_BUCKET='chillamyid-gemini-data'
export AR_REPO='chilla-myid-artifactregistry'  
export SERVICE_NAME='chilla-myid'

gcloud artifacts repositories create "$AR_REPO" --location="$GCP_REGION" --repository-format=Docker
gcloud auth configure-docker "$GCP_REGION-docker.pkg.dev"
gcloud builds submit --tag "$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME"

gcloud run deploy "$SERVICE_NAME" \
   --image="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME" \
   --region=$GCP_REGION \
   --project=$GCP_PROJECT \
   --set-env-vars=GCP_PROJECT=$GCP_PROJECT,GCP_REGION=$GCP_REGION,GCP_BUCKET=$GCP_BUCKET \
   --port=8080 \
   --allow-unauthenticated \
   --platform=managed  

#Result: 
#https://iamgemini-priyambodo-com-rzmyhdhywa-uc.a.run.app