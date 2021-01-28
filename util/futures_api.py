"python-binance Futures API wrapper."

import logging
from binance.client import Client

class Futures_Api():
    def __init__(self, client):
        assert isinstance(client, Client)
        self.__client = client
        self.__log = logging.getLogger("binance_api_wrapper")

    def positions(self):
        "Get all opened positions on Futures account from client."
        ret = []
        try:
            pos_info = self.__client.futures_position_information()
        except Exception as err: # pylint: disable=broad-except
            err_msg = f"`futures_position_information()` failed: {str(err)}"
            self.__log.warning(err_msg)
            return []

        # Get only opened positions
        for pos in pos_info:
            if float(pos["positionAmt"]) != 0.0:
                ret.append(pos)
        return ret

    def all_orders(self):
        "Get all orders on Futures account from client."
        try:
            return self.__client.futures_get_all_orders()
        except Exception as err: # pylint: disable=broad-except
            err_msg = f"`futures_get_all_orders()` failed: {str(err)}"
            self.__log.warning(err_msg)
            return {}

    def create_order(self, **order):
        "Create order on Futures account from client."
        try:
            _ = self.__client.futures_create_order(**order)
        except Exception as err: # pylint: disable=broad-except
            err_msg = f"`futures_create_order()` failed: {str(err)}"
            self.__log.warning(err_msg)

    def get_account(self):
        "Get Futures account from client."
        try:
            return self.__client.futures_account()
        except Exception as err: # pylint: disable=broad-except
            if "code=-2015" in str(err):
                # No futures account
                pass
            else:
                err_msg = f"`futures_account()` failed: {str(err)}"
                self.__log.warning(err_msg)
            return None
