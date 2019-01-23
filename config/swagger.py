swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger_template = {
  "swagger": "3.0",
  "info": {
    "title": "YOUR TITLE HERE",
    "description": "YOUR DESCRIPTION",
    "contact": {
      "responsibleOrganization": "AirAsia",
      "responsibleDeveloper": "Austin.g",
      "email": "austinzy@airasia.com"
    },
    "version": "0.0.1-dev"
  },
  "basePath": "/",  # base bash for blueprint registration
  "operationId": "enps_adhoc"
}