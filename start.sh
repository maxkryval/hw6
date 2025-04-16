#!/bin/bash
uvicorn db_service:app --host 0.0.0.0 --port 8001 &
sleep 1
uvicorn business_service:app --host 0.0.0.0 --port 8002 &
sleep 1
uvicorn client_service:app --host 0.0.0.0 --port 8000