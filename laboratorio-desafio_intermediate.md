
  LABORATÓRIO COM DESAFIO - Intermediate
  =====================================

  Develop GenAI Apps with Gemini and Streamlit: Challenge Lab
  --------------------------------------------------------------

  Tarefa 2
  --------
  
  O aplicativo com o radio button e o prompt:
  
 [chef.py](chef.py)


  Tarefa 3
  --------

```  
python3 -m venv gemini-streamlit
source gemini-streamlit/bin/activate
pip install -r requirements.txt
```
  
  definir as variáveis de ambiente:

```
GCP_PROJECT='Project ID'
GCP_REGION='Region'
```

  deve ficar assim:

```   
GCP_PROJECT='qwiklabs-gcp-01-d3a7a683c664'
GCP_REGION='us-central1'
```

   para executar o aplicativo:

```   
streamlit run chef.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
```

   para terminar a execução do aplicativo:

```   
   Ctrl + C
```

  Tarefa 4
  ---------

  O Dockerfile modificado para a execução do aplicativo chef.py:
  
 [Dockerfile](Dockerfile)

  Os comandos para a criação do repositório:

```  
  AR_REPO='chef-repo'
  SERVICE_NAME='chef-streamlit-app' 
  gcloud artifacts repositories create "$AR_REPO" --location="$GCP_REGION" --repository-format=Docker
  gcloud builds submit --tag "$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME"
```


   Tarefa 5
   --------

```   
gcloud run deploy "$SERVICE_NAME" \
  --port=8080 \
  --image="$GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$AR_REPO/$SERVICE_NAME" \
  --allow-unauthenticated \
  --region=$GCP_REGION \
  --platform=managed  \
  --project=$GCP_PROJECT \
  --set-env-vars=GCP_PROJECT=$GCP_PROJECT,GCP_REGION=$GCP_REGION
```

