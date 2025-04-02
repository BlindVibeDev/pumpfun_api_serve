@echo off
echo Starting PumpFun API Server...

cd "%~dp0"
wsl -e bash -c "cd \"/mnt/c/Users/wes7s/Pump Fun/pumpfun_api_server\" && source env/bin/activate && pip install -q fastapi uvicorn httpx python-dotenv && uvicorn main:app --host 0.0.0.0 --port 8000"

pause