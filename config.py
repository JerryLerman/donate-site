import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "fallback-dev-key")
    KOFI_URL = os.getenv("KOFI_URL", "")
    PATREON_URL = os.getenv("PATREON_URL", "")
    LIBERAPAY_URL = os.getenv("LIBERAPAY_URL", "")
    STRIPE_PAYMENT_URL = os.getenv("STRIPE_PAYMENT_URL", "")
    BTC_ADDRESS = os.getenv("BTC_ADDRESS", "")
    ETH_ADDRESS = os.getenv("ETH_ADDRESS", "")
