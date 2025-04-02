Write-Host "Setting up GitHub repository for PumpFun API Server..." -ForegroundColor Green

# Navigate to the script directory
Set-Location -Path $PSScriptRoot

# Add all files and commit
git add .
git commit -m "Update README and add LICENSE files"

Write-Host "`nCreating remote connection to GitHub..." -ForegroundColor Green
git remote add origin https://github.com/BlindVibeDev/pumpfun_api_server.git

Write-Host "`nPushing code to GitHub..." -ForegroundColor Green
git push -u origin main

Write-Host "`nSetup complete! Repository pushed to https://github.com/BlindVibeDev/pumpfun_api_server" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to continue..."