import ast
import os
import sqlite3
from typing import Any, Dict, List, Optional

# 1. FIXED: Hardcoded secret replaced with environment variable lookup
STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///users.db")


def register_user(
    username: str, 
    password: str, 
    roles: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    2. FIXED: Mutable default argument replaced with `None` sentinel.
    3. FIXED: SQL injection eliminated by using parameterized query (? placeholders).
    """
    if roles is None:
        roles = []

    # Using context manager for safe database connection lifecycle
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        # Parameterized query protects against SQL injection
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()

    roles.append("member")
    return {"status": "created", "roles": roles}


def execute_dynamic_calculation(formula: str, context: Optional[Dict[str, Any]] = None) -> Any:
    """
    4. FIXED: Dangerous eval() replaced with safe ast.literal_eval().
    5. FIXED: Bare except replaced with explicit exception types.
    """
    try:
        # ast.literal_eval only evaluates safe Python literals (numbers, strings, tuples, lists, dicts)
        return ast.literal_eval(formula)
    except (ValueError, SyntaxError, TypeError):
        # Specific exception handling prevents swallowing system interrupts
        return None
