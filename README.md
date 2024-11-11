

# **Hate Speech Classification Using RNN LSTM**

This project aims to classify hate speech in text data using a Recurrent Neural Network (RNN) architecture with **Long Short-Term Memory (LSTM)** cells. The goal is to accurately identify and categorize offensive or harmful content in user-generated text, such as social media posts or comments. The model is built with an **RNN-LSTM** architecture, chosen for its ability to capture long-term dependencies in sequential data, making it ideal for text classification tasks.

In addition to the core model, an **ETL** (Extract, Transform, Load) pipeline is developed to automate the process of collecting, preprocessing, and storing the data for training and evaluation from the **G-Cloud Storage**. The pipeline enables the efficient handling of large datasets and facilitates scalability and automation, key aspects of production-ready machine learning workflows.

## Key Components:
#### Data Collection (Extract):
Data is extracted from various sources (e.g., social media platforms, publicly available datasets, etc.) and ingested into Google Cloud Storage.

#### Data Transformation:
The raw data is cleaned and preprocessed, including tasks such as text tokenization, removing stopwords, stemming/lemmatization, and encoding labels. This step ensures that the data is in a format suitable for training the model.

#### Model Training:
The preprocessed data is fed into an RNN-LSTM architecture built with TensorFlow/Keras, which is designed to capture sequential dependencies in the text. Hyperparameter tuning is performed to improve model accuracy.

#### Model Evaluation:
The trained model is evaluated using standard classification metrics like accuracy, precision, recall, and F1-score. This step ensures that the model performs well in identifying hate speech and is generalizable across different types of text data.

#### Deployment:
The trained model is deployed for real-time classification of text input, allowing users to identify hate speech in new, unseen data.



## Technologies Used

**Programming Languages:** Python, HTML, Bash

**Libraries:** NumPy, Pandas, scikit-learn, NLTK, TensorFlow, Keras, Matplotlib,Flask,Git

**Cloud:** Google Cloud
## Folder Structure

![Folder Structure](https://raw.githubusercontent.com/Soumalla-Tarafder/Hate-Classification-Using-NLP/refs/heads/main/Flowcharts/1_Folder%20Structure.png)

## Data Ingestion Flowchart

![01_Data_Ingestion](https://raw.githubusercontent.com/Soumalla-Tarafder/Hate-Classification-Using-NLP/refs/heads/main/Flowcharts/01_Data_Ingestion.png)

## Data Transformation Flowchart

![02_Data_Transformation](https://raw.githubusercontent.com/Soumalla-Tarafder/Hate-Classification-Using-NLP/refs/heads/main/Flowcharts/02_Data_transformation.png)

## Model Trainer Flowchart

![03_Model_Trainer](https://raw.githubusercontent.com/Soumalla-Tarafder/Hate-Classification-Using-NLP/refs/heads/main/Flowcharts/03_Model_trainer.png)


## How To Start

```bash
conda create -n hate python=3.8 -y
```

```bash
conda activate hate
```

```bash
pip install -r requirements.txt
```
```bash
python app.py
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

- After Configure the gcp cloud with our gcp cli 

- Their have one alternate way to upload the data to gcp cloud using sync_folder_to_gcloud method written in configuration folder inside gsync file.

- For Download the data from gcloud we use sync_folder_from_gcloud method from configuration folder inside gsync file.

## License

[Apache 2.0](http://www.apache.org/licenses/)


