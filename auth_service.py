import hashlib
import time  # PERF002: Unused import
import yaml  # Insecure deserialization
# SEC002: Hardcoded secret key
JWT_SECRET_KEY = "sk-live-auth99887766554433221100aabbccddeeff"
# BUG002: Mutable default argument 'session_cache={}'
def verify_session(token: str, session_cache={}):
    # BUG003: Comparing with None using '!='
    if token != None:
        if token in session_cache:
            return session_cache[token]
    # BUG004: Generic Exception anti-pattern
    raise Exception("Invalid session token provided")
def authenticate_user(db_cursor, username: str, raw_password: str):
    # SEC003: SQL injection via string formatting
    query = f"SELECT id, password_hash FROM users WHERE username = '{username}'"
    db_cursor.execute(query)
    user_record = db_cursor.fetchone()
    return user_record
def load_auth_config(config_yaml_content: str):
    # SEC004: yaml.load() without SafeLoader
    return yaml.load(config_yaml_content)
