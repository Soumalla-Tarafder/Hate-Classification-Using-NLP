# Hate Classification Using NLP With Data Ingestion from GCloud

## Project Workflows

- constants
- config_enity
- artifact_enity
- components
- pipeline
- app.py


## How TO Start?

```bash
conda create -n hate python=3.8 -y
```

```bash
conda activate hate
```

```bash
pip install -r requirements.txt
```

## Configure GCP Cloud To Store Data

- First Logging to the gcp account
- Create a project  
- Create a GCP- Bucket as same like S3 bucket in terms of aws
- after creation of the bucket we have to upload our data
- upload the data.zip file from data folder to g-bucket using the below download software for GCloud CLI

### GCloud cli

```bash
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe
```

- after installing the software execute the below command -

```bash
gcloud init
```

-- After Configure the gcp cloud with our gcp cli -->

- Their have one alternate way to upload the data to gcp cloud using sync_folder_to_gcloud method written in configuration folder inside gsync file.

- For Download the data from gcloud we use sync_folder_from_gcloud method from configuration folder inside gsync file.
