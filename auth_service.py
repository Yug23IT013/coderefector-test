import os
import yaml
from typing import Optional, Dict, Any

class SessionValidationError(Exception):
    """Specific exception for invalid session states."""
    pass

# Fixed SEC002: Secret fetched safely from environment variables
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "")

# Fixed BUG002 & BUG003: Default initialized as None, checked using 'is not None'
def verify_session(token: Optional[str], session_cache: Optional[Dict[str, Any]] = None) -> Any:
    if session_cache is None:
        session_cache = {}

    if token is not None:
        if token in session_cache:
            return session_cache[token]

    # Fixed BUG004: Raises specific custom exception instead of generic Exception
    raise SessionValidationError("Invalid session token provided")

def authenticate_user(db_cursor, username: str, raw_password: str):
    # Fixed SEC003: Parameterized SQL query prevents SQL injection
    query = "SELECT id, password_hash FROM users WHERE username = ?"
    db_cursor.execute(query, (username,))
    user_record = db_cursor.fetchone()
    return user_record

def load_auth_config(config_yaml_content: str):
    # Fixed SEC004: SafeLoader prevents arbitrary object instantiation
    return yaml.safe_load(config_yaml_content)
