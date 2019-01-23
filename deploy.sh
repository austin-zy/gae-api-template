#!/usr/bin/env bash
pip freeze > requirements.txt
gcloud app deploy