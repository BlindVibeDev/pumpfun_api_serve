"""
Mock data module for PumpFun API Server
"""

# Featured tokens mock data for demonstration/testing
FEATURED_TOKENS = [
    {
        "mint": "GK3Mi7bZY5ccgeeZCzNDvc4WZFQoqKSSWHJ6e44JfjZW",
        "name": "PumpPortal",
        "symbol": "PORTAL",
        "price": 0.00124,
        "change_24h": 5.2,
        "volume_24h": 15432,
        "market_cap": 248760
    },
    {
        "mint": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        "name": "Bonk",
        "symbol": "BONK",
        "price": 0.00000234,
        "change_24h": -2.1,
        "volume_24h": 987654,
        "market_cap": 23450000
    },
    {
        "mint": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
        "name": "Marinade Staked SOL",
        "symbol": "mSOL",
        "price": 134.56,
        "change_24h": 0.8,
        "volume_24h": 2345678,
        "market_cap": 456789123
    }
]

# Token details mock data for demonstration/testing
TOKEN_DETAILS = {
    "GK3Mi7bZY5ccgeeZCzNDvc4WZFQoqKSSWHJ6e44JfjZW": {
        "mint": "GK3Mi7bZY5ccgeeZCzNDvc4WZFQoqKSSWHJ6e44JfjZW",
        "name": "PumpPortal",
        "symbol": "PORTAL",
        "price": 0.00124,
        "change_24h": 5.2,
        "volume_24h": 15432,
        "market_cap": 248760,
        "description": "PumpPortal is a Solana token trading platform API",
        "liquidity": 125000,
        "holders": 1250,
        "chart_data": [
            {"timestamp": "2023-01-01", "price": 0.00100},
            {"timestamp": "2023-01-02", "price": 0.00115},
            {"timestamp": "2023-01-03", "price": 0.00120},
            {"timestamp": "2023-01-04", "price": 0.00124}
        ]
    },
    "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU": {
        "mint": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        "name": "Bonk",
        "symbol": "BONK",
        "price": 0.00000234,
        "change_24h": -2.1,
        "volume_24h": 987654,
        "market_cap": 23450000,
        "description": "Bonk is a community-focused memecoin on Solana",
        "liquidity": 4567890,
        "holders": 125000,
        "chart_data": [
            {"timestamp": "2023-01-01", "price": 0.00000250},
            {"timestamp": "2023-01-02", "price": 0.00000245},
            {"timestamp": "2023-01-03", "price": 0.00000240},
            {"timestamp": "2023-01-04", "price": 0.00000234}
        ]
    },
    "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So": {
        "mint": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
        "name": "Marinade Staked SOL",
        "symbol": "mSOL",
        "price": 134.56,
        "change_24h": 0.8,
        "volume_24h": 2345678,
        "market_cap": 456789123,
        "description": "Marinade is a liquid staking protocol for Solana",
        "liquidity": 98765432,
        "holders": 34567,
        "chart_data": [
            {"timestamp": "2023-01-01", "price": 131.20},
            {"timestamp": "2023-01-02", "price": 132.45},
            {"timestamp": "2023-01-03", "price": 133.78},
            {"timestamp": "2023-01-04", "price": 134.56}
        ]
    }
}