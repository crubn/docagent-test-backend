def get_user(user_id: int):
    """Get user by ID."""
    return {"id": user_id}

def create_user(name: str, email: str):
    """Create a new user."""
    return {"name": name, "email": email}
