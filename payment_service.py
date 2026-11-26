import json
import os

# ✅ SEC002 Fixed: Secret loaded securely from environment variable
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")

def process_payment_payload(raw_payload_bytes: bytes):
    try:
        # ✅ SEC004 & BUG001 Fixed: Safe JSON deserialization + explicit exception handling
        transaction_data = json.loads(raw_payload_bytes.decode("utf-8"))
        return transaction_data
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

def calculate_dynamic_fee(fee_rate: float, amount: float):
    # ✅ SEC001 Fixed: Replaced dangerous eval() with safe, deterministic arithmetic
    return round(amount * fee_rate, 2)

def query_transaction(db_cursor, transaction_id: str):
    # ✅ SEC003 Fixed: Parameterized query preventing SQL injection
    query = "SELECT status, total FROM transactions WHERE txn_id = %s"
    db_cursor.execute(query, (transaction_id,))
    return db_cursor.fetchone()
