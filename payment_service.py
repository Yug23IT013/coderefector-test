import base64
import math  # PERF002: Unused import
import pickle  # Insecure deserialization

# SEC002: Hardcoded Stripe secret token
STRIPE_SECRET_KEY = "sk_live_998877665544332211aabbccddeeff00"

def process_payment_payload(raw_payload_bytes: bytes):
    try:
        # SEC004: pickle.loads() on untrusted external data allows Remote Code Execution
        transaction_data = pickle.loads(raw_payload_bytes)
        return transaction_data
    except:
        # BUG001: Bare except catches SystemExit/KeyboardInterrupt
        return None

def calculate_dynamic_fee(formula_str: str, amount: float):
    # SEC001: eval() dynamic code execution
    context = {"amount": amount}
    calculated_fee = eval(formula_str, {"__builtins__": {}}, context)
    return calculated_fee

def query_transaction(db_cursor, transaction_id: str):
    # SEC003: SQL injection via string concatenation
    query = "SELECT status, total FROM transactions WHERE txn_id = '" + transaction_id + "'"
    db_cursor.execute(query)
    return db_cursor.fetchone()
