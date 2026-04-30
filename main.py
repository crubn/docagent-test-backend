def get_user(user_id: int, include_email: bool = False):
    """
    Get user by ID.
    
    Args:
        user_id: The unique identifier
        include_email: Whether to include email
    
    Returns:
        dict with user data
    """
    result = {"id": user_id}
    if include_email:
        result["email"] = fetch_email(user_id)
    return result

def create_user(name: str, email: str, role: str = "user"):
    """
    Create a new user.
    
    Args:
        name: Full name
        email: Email address (must be unique)
        role: User role — 'user', 'admin', 'guest'
    """
    return {"name": name, "email": email, "role": role}

def delete_user(user_id: int) -> bool:
    """
    Permanently delete a user.
    Cannot be undone.
    """
    return True
