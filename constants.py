import os

# Environment variables

ACCOUNTS = {
    "napcopy": {
        "key": os.getenv("BINANCE_NAPCOPY_KEY"),
        "secret": os.getenv("BINANCE_NAPCOPY_SECRET")
    },
    "master": {
        "key": os.getenv("BINANCE_MAIN_KEY"),
        "secret": os.getenv("BINANCE_MAIN_SECRET")
    }
}
