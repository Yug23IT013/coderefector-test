import pickle

# ❌ SEC002 [Critical]: Hardcoded secret still present
STRIPE_SECRET_KEY = "sk_live_998877665544332211aabbccddeeff00"

def process_payment_payload(raw_payload_bytes: bytes):
    try:
        # ❌ SEC004 [Critical]: Insecure pickle deserialization still present
        transaction_data = pickle.loads(raw_payload_bytes)
        return transaction_data
    except Exception:
        # ✅ BUG001 Fixed: Catching specific Exception instead of bare except
        return None

def calculate_dynamic_fee(formula_str: str, amount: float):
    # ❌ SEC001 [Critical]: eval() dynamic execution still present
    context = {"amount": amount}
    calculated_fee = eval(formula_str, {"__builtins__": {}}, context)
    return calculated_fee

def query_transaction(db_cursor, transaction_id: str):
    # ✅ SEC003 Fixed: Parameterized query placeholder used instead of string concatenation
    query = "SELECT status, total FROM transactions WHERE txn_id = %s"
    db_cursor.execute(query, (transaction_id,))
    return db_cursor.fetchone()
