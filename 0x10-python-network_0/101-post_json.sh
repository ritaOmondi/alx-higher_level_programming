#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response
URL="$1"
JSON_FILE="$2"

# Check if the JSON file is valid
if ! python3 -m json.tool "$JSON_FILE" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request and display response body
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"

