# Austin API Template
This is Austin's way/template of creating microservice, using

  - Flask (Backend Framework)
  - Flasgger (Documentation)
  -- https://github.com/rochacbruno/flasgger
  - Blueprint (Optional, used when there are many endpoints)
  -- http://flask.pocoo.org/docs/1.0/blueprints/

## Project Name Convention
**Project Name**: gae-XXXXX

## Authentication
If authentication is needed, use JWT Authentication.
With Header
```
Authorization: Bearer xxxxxxx
```
https://pythonhosted.org/Flask-JWT/
example will be given later on

## Explanation of each folder
- **assets/**
--  Sometimes you will have png, csv, ... or any large file (>0.5MB, such as documents, images, ...). Place all of them here.
- **auth/**
-- When you have credentials file, especially when you using GCP (BQ, Firestore, ...), place them inside this folder. Generate the credential file (.json) from the IAM management(Service Account) in GCP Console.
-- Most of the time, you just need to call the client by
```
abc_client = abc.Client().from_service_account_json("auth/your_service_account.json")
```
- **config**
-- A place for you to store all the configuration such as swagger configurations or any other configuration
- **helpers**
-- Provide abstraction to many functions to make code look cleaner. If you have reusable codes/functions that needed to be applied in many place. Place them inside here. 
-- Normally I will include a utils_helper/misc_helper for all the common functions (such as get_country_code, get_standard_datetime, ....)
- **documentations**
-- Place all the swagger/flasgger documentations (.yml) inside here.
- **controllers**
-- Also for abstraction to avoid main.py to be very lengthy.
- **app.yaml**
-- Configuration file for AppEngine, deploy by gcloud app deploy
-- If this is very important project where testing is needed, split to stg.yaml and prod.yaml so that you can deploy by gcloud app deploy stg.yaml/gcloud app deploy.prod.yaml
-- We can also write a bash script for deploying app.yaml (I always forget to pip freeze > requirements.txt before deploying) = deploy.sh
- **main.py**
-- the entrypoint for API
-- chatbot_entrypoint() : Because chatbot can only serve one webhook endpoint, so you need to use "action" to redirect to correct functions

## Python Code Convention
https://www.python.org/dev/peps/pep-0008/

## API Documentations
https://github.com/rochacbruno/flasgger

## Exception/ Error Handlers
http://flask.pocoo.org/docs/0.12/patterns/errorpages/#error-handlers

## CORS
Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP headers to tell a browser to let a web application running at one origin (domain) have permission to access selected resources from a server at a different origin. A web application makes a cross-origin HTTP request when it requests a resource that has a different origin (domain, protocol, and port) than its own origin.
CORS for Flask: https://flask-cors.readthedocs.io/en/latest/

## Development
```
python main.py
```

## Deployment
```
./deploy.sh
```

## Versioning
Semantic Versioning: https://semver.org/

## GAE Config
https://cloud.google.com/appengine/docs/standard/python/config/appref

## FAQ
1. Difference between yaml and yml file
- No difference
2. With file: ...yml, do we call it?
- For app.yaml: gcloud app deploy will read the file
- For documentations/*.yml: flasgger will read it
3. Best way of storing authentication token
- To avoid exposing token in deployment code, people usually save authentication token or any sensitive token/password in environment variables, such as
```
# Declaring the environment variables in OS inside app.yaml
env_variables:
  BQ_AUTH:ABCDSADSADSADSAD
```
```
# Get the token from using os.environ
bq_auth = os.environ["BQ_AUTH"]
```
- Another reason why we need this is to specify staging environment and production environment. for e.g. in staging we use different table for logging/or project, in production we use different project, then we need different auth. Thus we can place it inside the OS environment variables and use stg.yaml/prod.yaml to control them
4. GCP Products
- Cloud task
-- Cloud task is used when running long query(> 10s), so that it can scale in the background. And of course, only for side effect call or async call, not for blocking call
- Big Query
-- Normally use for logging purposes. Use tylertreat/bigquery-python library
- Spreadsheet
-- Realtime Frontend Editing UI. Use gspread library
- Firestore/Datastore
-- To store, retrieve, edit data
- Redis
-- For caching in memory, especially with expiry time
5. How to write the required yml files?
- app.yaml/stg.yaml/prod.yml
-- Just copy and paste
- Documentations
-- Refer to flasgger site,https://github.com/rochacbruno/flasgger or openapi specs
6. How to change project? for e.g. airasia-datascience-stg -> airasia-datascience
```
gcloud config set project xxxxxxxxxxxx
```
