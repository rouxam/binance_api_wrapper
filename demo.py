"Demo of spot and futures APIs"

# Libraries
import logging
from binance.client import Client

# Local imports
from util import Spot_Api, Futures_Api
from constants import ACCOUNTS

# Setup loggier
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("binance_api_wrapper")

def main():
    "Main demo method."
    for account, api in ACCOUNTS.items():
        LOG.info("*****")
        LOG.info("Account %s", account)
        LOG.info("*****")
        client = Client(api["key"], api["secret"])
        spot = Spot_Api(client)
        futures = Futures_Api(client)

        # Calling and priting a few stuff for demo
        all_spot_orders = spot.get_all_orders("BTCUSDT")
        LOG.info("Last BTCUSDT order on spot account: %s", all_spot_orders[-1:])

        opened_positions = futures.positions()
        LOG.info("Opened positions on Futures account: %s", opened_positions)

        all_futures_orders = futures.all_orders()
        LOG.info("Last BTCUSDT order on Futures account: %s", all_futures_orders[-1:])

if __name__ == "__main__":
    main()
