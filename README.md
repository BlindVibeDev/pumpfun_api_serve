# Pump.fun API Server

A FastAPI server that interacts with the Pump.fun API for trading tokens using the PumpPortal API.

## Quick Start

1. Double-click the `run.bat` file to start the server
2. The server will be available at http://localhost:8000
3. Access the API documentation at http://localhost:8000/docs

## Environment Configuration

The API is pre-configured with your PumpPortal credentials:

- API Key: Configured in .env file
- Wallet Public Key: 5YYgQY4dD8wk3mpABJauT569T4wcE4MGbtdkJ4HSdr7g
- Default API Username: admin
- Default API Password: changeme

## API Endpoints

### Trading

- `POST /trade`: Execute buy/sell trades on Pump.fun

Example request:
```json
{
  "action": "buy",
  "mint": "token_contract_address_here",
  "amount": 1.0,
  "denominated_in_sol": true,
  "slippage": 0.5,
  "priority_fee": 0.00001,
  "pool": "pump"
}
```

### Token Information

- `GET /tokens/featured`: Get a list of featured tokens
- `GET /token/{mint}`: Get information about a specific token

## Security

All endpoints are protected with HTTP Basic Authentication using the credentials:
- Username: admin
- Password: changeme 

You can change these in the .env file if needed.

## Accessing from Other Devices

The server runs on all interfaces (0.0.0.0) so you can access it from other devices on your local network using your computer's IP address:

http://your-ip-address:8000/docs

If you need to access it over the internet, consider using a service like ngrok.