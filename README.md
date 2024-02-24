# NLP-Project-With-Full-Pipeline

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
