#!/bin/bash

# Step 1: Build the image
podman build -t hw5-app .

# Step 2: Run the container
podman run -d --name hw5-container -p 8000:8000 -p 8001:8001 -p 8002:8002 hw5-app

# Step 3: Test the service
curl http://localhost:8000/

# Step 4: View logs
podman logs hw5-container

# Step 5: Clean up
podman stop hw5-container
podman rm hw5-container
podman rmi hw5-app