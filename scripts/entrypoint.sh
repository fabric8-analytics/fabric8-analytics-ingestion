#!/usr/bin/bash

# Start API ingestion service with time out
gunicorn --pythonpath /f8a_ingestion/ -b 0.0.0.0:$INGESTION_API_SERVICE_PORT -t $INGESTION_API_SERVICE_TIMEOUT -k $CLASS_TYPE -w $NUMBER_WORKER_PROCESS rest_api:app