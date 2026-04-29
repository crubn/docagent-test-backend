def get_user(user_id: int, include_email: bool = False):
    """
    Get user by ID.

    Args:
        user_id: The unique identifier of the user
        include_email: Whether to include email in response
    """
    result = {"id": user_id}
    if include_email:
        result["email"] = fetch_email(user_id)
    return result

def create_user(name: str, email: str, role: str = "user"):
    """
    Create a new user.

    Args:
        name: Full name of the user
        email: Email address (must be unique)
        role: User role, defaults to 'user'
    """
    return {"name": name, "email": email, "role": role}

def delete_user(user_id: int) -> bool:
    """Delete user permanently. This cannot be undone."""
    return True

class UserService:
    """Service for managing users."""

    def __init__(self, db, cache=None):
        self.db = db
        self.cache = cache

    def find_by_email(self, email: str):
        """Find user by email address."""
        return self.db.query(email)

    def bulk_delete(self, user_ids: list[int]) -> int:
        """Delete multiple users. Returns count deleted."""
        return len(user_ids)
