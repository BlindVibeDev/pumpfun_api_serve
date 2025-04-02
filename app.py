from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import httpx
import os
import secrets
from typing import Annotated
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import logging

# Import mock data for testing
from mock_data import FEATURED_TOKENS, TOKEN_DETAILS

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("pumpfun-api")

# Load environment variables from .env file
load_dotenv()
logger.info("Starting PumpFun API Server")

# Create application
app = FastAPI(
    title="PumpFun API Server",
    description="A FastAPI server for interacting with Pump.fun API",
    version="1.0.0",
)

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBasic()

# API credentials from environment variables
API_USERNAME = os.getenv("API_USERNAME", "admin")
API_PASSWORD = os.getenv("API_PASSWORD", "changeme")

# PumpPortal API credentials
PUMPPORTAL_API_KEY = os.getenv("PUMPPORTAL_API_KEY")
WALLET_PUBLIC_KEY = os.getenv("WALLET_PUBLIC_KEY")

# Log API key status (but not the actual key for security)
if PUMPPORTAL_API_KEY:
    logger.info("PumpPortal API key loaded")
else:
    logger.error("PumpPortal API key not found in environment variables")

if WALLET_PUBLIC_KEY:
    logger.info(f"Wallet public key loaded: {WALLET_PUBLIC_KEY}")
else:
    logger.error("Wallet public key not found in environment variables")

# Authentication function
def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = API_USERNAME.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = API_PASSWORD.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# PumpPortal API base URL
PUMPPORTAL_BASE_URL = "https://pumpportal.fun/api"

# API models
class Token(BaseModel):
    mint: str
    name: str = None
    symbol: str = None

@app.get("/", tags=["Info"])
def read_root():
    return {"message": "Welcome to the PumpFun API Server. See /docs for API documentation."}

class TradeRequest(BaseModel):
    action: str
    mint: str
    amount: float
    denominated_in_sol: bool
    slippage: float
    priority_fee: float
    pool: str = "pump"

@app.post("/trade", tags=["Trading"])
async def trade(
    request: TradeRequest,
    username: str = Depends(get_current_username)
):
    """
    Execute a trade on Pump.fun.

    Parameters:
    - action: "buy" or "sell"
    - mint: The contract address of the token to trade
    - amount: The amount of SOL or tokens to trade
    - denominated_in_sol: True if amount is in SOL, False if in tokens
    - slippage: The percent slippage allowed
    - priority_fee: Amount to use as priority fee
    - pool: The exchange to trade on ("pump", "raydium", "pump-amm", or "auto")
    """
    if request.action not in ["buy", "sell"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid action. Must be 'buy' or 'sell'.")

    trade_data = {
        "publicKey": WALLET_PUBLIC_KEY,
        "action": request.action,
        "mint": request.mint,
        "amount": request.amount,
        "denominatedInSol": request.denominated_in_sol,
        "slippage": request.slippage,
        "priorityFee": request.priority_fee,
        "pool": request.pool
    }

    headers = {
        "Authorization": f"Bearer {PUMPPORTAL_API_KEY}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{PUMPPORTAL_BASE_URL}/trade-local", json=trade_data, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.get("/tokens/featured", tags=["Tokens"])
async def get_featured_tokens(
    username: str = Depends(get_current_username)
):
    """Get a list of featured tokens from PumpPortal"""
    logger.info("Getting featured tokens")
    
    # Use the imported mock data
    return FEATURED_TOKENS
    
    # When ready to use the real API with PumpPortal:
    # headers = {
    #     "Authorization": f"Bearer {PUMPPORTAL_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(f"{PUMPPORTAL_BASE_URL}/featured-tokens", headers=headers)
    #     if response.status_code != 200:
    #         raise HTTPException(status_code=response.status_code, detail=response.text)
    #     return response.json()

@app.get("/token/{mint}", tags=["Tokens"])
async def get_token_info(
    mint: str,
    username: str = Depends(get_current_username)
):
    """Get information about a specific token by mint address"""
    logger.info(f"Getting token info for {mint}")
    
    # Check if we have mock data for this mint
    if mint in TOKEN_DETAILS:
        return TOKEN_DETAILS[mint]
    
    # For unknown tokens, return a generic response
    return {
        "mint": mint,
        "name": "Unknown Token",
        "symbol": "???",
        "price": 0.0001,
        "change_24h": 0.0,
        "message": "This is mock data for demonstration"
    }
    
    # When ready to use the real API with PumpPortal:
    # headers = {
    #     "Authorization": f"Bearer {PUMPPORTAL_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(f"{PUMPPORTAL_BASE_URL}/token/{mint}", headers=headers)
    #     if response.status_code != 200:
    #         raise HTTPException(status_code=response.status_code, detail=response.text)
    #     return response.json()