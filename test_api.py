import httpx
import asyncio
import json

async def test_api_server():
    base_url = "http://localhost:8000"
    
    print("Testing PumpFun API Server...")
    
    # Test 1: Root endpoint
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{base_url}/", auth=("admin", "changeme"))
            print("\n1. Root Endpoint Test:")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error accessing root endpoint: {e}")
    
    # Test 2: Featured tokens
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{base_url}/tokens/featured", auth=("admin", "changeme"))
            print("\n2. Featured Tokens Test:")
            print(f"Status: {response.status_code}")
            data = response.json()
            print(f"Number of featured tokens: {len(data)}")
            if len(data) > 0:
                print(f"Sample token data: {json.dumps(data[0], indent=2)}")
                print("Successfully received token data that can be used in your frontend!")
        except Exception as e:
            print(f"Error accessing featured tokens: {e}")
    
    # Test 3: Get a specific token
    # Using a known token mint address
    sample_token_mint = "GK3Mi7bZY5ccgeeZCzNDvc4WZFQoqKSSWHJ6e44JfjZW"  # PumpPortal token
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{base_url}/token/{sample_token_mint}", auth=("admin", "changeme"))
            print("\n3. Token Info Test:")
            print(f"Status: {response.status_code}")
            data = response.json()
            print(f"Token data: {json.dumps(data, indent=2)}")
            print("Successfully received detailed token data that can be used in your frontend!")
        except Exception as e:
            print(f"Error accessing token info: {e}")
    
    print("\nTests completed!")

if __name__ == "__main__":
    asyncio.run(test_api_server())