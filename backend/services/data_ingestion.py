import requests
import asyncio
from backend.core.config import settings
from backend.db.connection import get_timescale_pool
from backend.core.logging import logger

async def fetch_stock(symbol: str):
    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={settings.FINNHUB_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Fetched data for {symbol}: {data}")
        return {
            "symbol": symbol,
            "price": data.get("c"),
            "high": data.get("h"),
            "low": data.get("l"),
            "volume": data.get("v")
        }
    except Exception as e:
        logger.error(f"Failed to fetch data for {symbol}: {e}")
        return None

async def insert_stock_data(pool, record):
    if record:
        async with pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO stock_prices (symbol, price, high, low, volume, timestamp)
                VALUES ($1, $2, $3, $4, $5, NOW())
                """,
                record["symbol"], record["price"], record["high"], record["low"], record["volume"]
            )
        logger.info(f"Inserted data for {record['symbol']} into database.")

async def ingest_all(symbols=["AAPL", "TSLA", "GOOG"]):
    logger.info("Starting data ingestion process...")
    pool = await get_timescale_pool()
    for symbol in symbols:
        data = await fetch_stock(symbol)
        await insert_stock_data(pool, data)
    await pool.close()
    logger.info("Data ingestion process completed.")

if __name__ == "__main__":
    asyncio.run(ingest_all())
