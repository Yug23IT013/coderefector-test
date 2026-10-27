import os
from typing import Optional, Dict

class AuthenticationError(Exception):
    """Custom exception for authentication failures."""
    pass

# BUG002: Mutable default argument 'cache={}'
def get_cached_user(user_id: str, cache: Dict[str, str] = {}) -> Optional[str]:
    if user_id in cache:
        return cache[user_id]
    
    # Simulate lookup
    token = os.environ.get("DEFAULT_USER_TOKEN")
    if token is not None:
        cache[user_id] = token
        return token
    
    raise AuthenticationError(f"User {user_id} not found in cache or environment.")
