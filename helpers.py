def parse_amount_currency(text):
    parts = text.strip().split()
    if len(parts) == 2:
        try:
            amount = float(parts[0])
            currency = parts[1].upper()
            return amount, currency
        except ValueError:
            return None, None
    return None, None
