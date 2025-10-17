import asyncio
from backend.services.data_ingestion import ingest_all
from backend.services.celery_app import app

# Celery task to run ingestion
@app.task
def scheduled_ingestion(symbols=None):
    if symbols is None:
        symbols = ["AAPL", "TSLA", "GOOG"]  # default watchlist
    asyncio.run(ingest_all(symbols))
