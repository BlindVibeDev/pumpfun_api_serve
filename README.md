# Pump.fun API Server

A FastAPI server that interacts with the Pump.fun API for trading tokens using the PumpPortal API.

## Features

- Secure API with HTTP Basic Authentication
- Trading endpoints for buying and selling tokens
- Token information endpoints with mock data
- Interactive API documentation with Swagger UI
- Cross-origin support for frontend integration

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/BlindVibeDev/pumpfun_api_server.git
   cd pumpfun_api_server
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn httpx python-dotenv
   ```

4. Create a `.env` file with your credentials:
   ```
   PUMPPORTAL_API_KEY=your_api_key_here
   WALLET_PUBLIC_KEY=your_wallet_public_key_here
   API_USERNAME=admin
   API_PASSWORD=changeme
   ```

5. Run the server:
   ```bash
   # For development
   uvicorn app:app --reload
   
   # For production
   uvicorn app:app --host 0.0.0.0
   ```
   
   Or simply run the included `run_fixed.bat` file on Windows.

## API Endpoints

The API documentation is available at `/docs` when the server is running.

### Authentication

All endpoints are protected with HTTP Basic Authentication. You need to provide the username and password set in your environment variables.

### Trading Endpoints

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

### Token Information Endpoints

- `GET /tokens/featured`: Get a list of featured tokens
- `GET /token/{mint}`: Get information about a specific token

## Testing

You can run the included test script to verify the API is working:

```bash
python test_api.py
```

## Production Deployment

For production environments, it's recommended to:

1. Change default authentication credentials
2. Set up HTTPS using a reverse proxy
3. Restrict CORS origins to only trusted domains

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.