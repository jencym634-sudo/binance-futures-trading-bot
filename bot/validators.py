def validate_order(symbol, side, order_type, quantity, price):
    
    valid_sides = ["BUY", "SELL"]
    valid_types = ["MARKET", "LIMIT"]

    if side not in valid_sides:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in valid_types:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")
