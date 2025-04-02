#!/bin/bash

echo "Setting up GitHub repository for PumpFun API Server..."

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Add all files and commit
git add .
git commit -m "Update README and add LICENSE files"

echo
echo "Creating remote connection to GitHub..."
git remote add origin https://github.com/BlindVibeDev/pumpfun_api_server.git

echo
echo "Pushing code to GitHub..."
git push -u origin main

echo
echo "Setup complete! Repository pushed to https://github.com/BlindVibeDev/pumpfun_api_server"
echo

read -p "Press Enter to continue..."