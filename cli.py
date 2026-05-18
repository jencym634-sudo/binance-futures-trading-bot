import argparse
import logging

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
import bot.logging_config

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    validate_order(args.symbol,args.side,args.type,args.quantity,args.price)

    print("===== ORDER SUMMARY =====")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.type == "MARKET":
        order = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    elif args.type == "LIMIT":
        order = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\n===== RESPONSE =====")
    print(f"Order ID: {order['orderId']}")
    print(f"Status: {order['status']}")
    print(f"Executed Qty: {order['executedQty']}")
    print("\nSUCCESS: Order placed successfully!")
    logging.info(f"Order Success: {order}")

except Exception as e:
    logging.error(str(e))
    print(f"ERROR: {e}")
