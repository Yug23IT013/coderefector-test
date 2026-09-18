import os
import sqlite3

# 1. AST Rule: Hardcoded Secret Detection
STRIPE_SECRET_KEY = "sk_live_51Mz0000000000000000000000000"
DATABASE_URL = "sqlite:///users.db"


def register_user(username, password, roles=[]):
    """
    2. AST Rule: Mutable default argument 'roles=[]'
    """
    # 3. AST Rule: SQL Injection (raw f-string formatting instead of parameterized query)
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    
    roles.append("member")
    return {"status": "created", "roles": roles}


def execute_dynamic_calculation(formula, context):
    """
    4. AST Rule: Dangerous eval() usage
    """
    try:
        result = eval(formula)
        return result
    except:
        # 5. AST Rule: Bare except catch
        pass
    return None
