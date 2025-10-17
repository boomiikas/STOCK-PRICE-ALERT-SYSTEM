from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(
    f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@localhost:27017/?authSource=admin"
)
db = client["stock_app"]

# Collections
users_col = db["users"]
alerts_col = db["alerts"]

# User Example: email, phone_number, watchlist, thresholds
def create_user(email: str, phone_number: str, watchlist=None, thresholds=None):
    if watchlist is None:
        watchlist = []
    if thresholds is None:
        thresholds = {}
    users_col.insert_one({
        "email": email,
        "phone_number": phone_number,
        "watchlist": watchlist,
        "thresholds": thresholds
    })

# AlertLog Example: user_id, symbol, type, timestamp
def create_alert(user_id, symbol, alert_type):
    from datetime import datetime
    alerts_col.insert_one({
        "user_id": user_id,
        "symbol": symbol,
        "type": alert_type,
        "timestamp": datetime.utcnow()
    })
