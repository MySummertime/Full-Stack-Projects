#!/bin/bash

# Step 1: activate virtual environment
# Check if virtual environment is activated
if [[ -z "${VIRTUAL_ENV}" ]]; then
    # Activate virtual environment
    source ./venv/bin/activate
fi

# Step 2: download requirements
pip install -r requirements.txt

# Step 3: set up environment variables
while IFS = read -r line; do
    export "$line"
done < .env

# Step 4: activate web server
univorn main:app --port 9090